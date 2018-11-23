package dataexporter;

import com.mongodb.MongoClient;
import com.mongodb.MongoClientURI;

import com.mongodb.client.MongoDatabase;
import com.mongodb.client.MongoCollection;

import org.bson.Document;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Random;
import java.util.Set;

public class Creator {

    public MongoDatabase getDatabase() {
        return database;
    }

    public MongoCollection<Document> getCollection() {
        return collection;
    }

    public MongoClient getMongoClient() {
        return mongoClient;
    }

    private MongoDatabase database;
    private MongoCollection<Document> collection;
    private MongoClient mongoClient;

    private BufferedReader br = null;
    private String line = "";
    private String cvsSplitBy = ",";

    public Creator(String clientConnectionString, String collectionName) {
        mongoClient = new MongoClient(new MongoClientURI(clientConnectionString));
        database = mongoClient.getDatabase("familyfeuddb");

        if (database.getCollection(collectionName) != null){
            database.getCollection(collectionName).drop();
        }

        database.createCollection(collectionName);
        collection = database.getCollection(collectionName);
    }

    public boolean importCSV(String inputFileName){

        if (database == null){
            return false;
        }

        if (collection == null){
            return false;
        }
        List<Document> questionDocumentList = new ArrayList<Document>();
        try {

            br = new BufferedReader(new FileReader(inputFileName));
            int lineNumber = 0;
            Document doc;

            while ((line = br.readLine()) != null) {

                // use comma as separator
                String[] question = line.split(cvsSplitBy);
                if (lineNumber == 0){
                    lineNumber = 1;
                    continue;
                }

                doc = new Document("question", question[0]);
                List<String> answer = new ArrayList<String>(); 
                List<String> pointsanswer = new ArrayList<String>(); 

                doc.append("questionID", lineNumber);
                for (int i = 1; i < question.length; i++){
                    if (i % 2 ==0){
                        pointsanswer.add(question[i]);
                    } else {
                        answer.add(question[i]); 
                    }
                }
                doc = doc.append("pointsanswer", pointsanswer);
                doc = doc.append("answer", answer);
                questionDocumentList.add(doc);
                lineNumber++;
            }
            doc = new Document("lineCount", lineNumber);
            questionDocumentList.add(doc);

            this.collection.insertMany(questionDocumentList);

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (br != null) {
                try {
                    br.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
        return true;
    }

}
