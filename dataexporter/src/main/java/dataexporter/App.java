package dataexporter;

import java.util.Scanner;

public final class App {
    private static Creator creator;

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        String connectionString = "";
        String collectionName = "";

        if (args.length != 0) {
            connectionString = args[0];
            collectionName = args[1];
        }

        if (connectionString == "" || collectionName == ""){
            System.out.print("Mongo Connection String: ");
            connectionString = scanner.nextLine();

            System.out.print("Collection Name: ");
            collectionName = scanner.nextLine();
        }

        if (connectionString == null) {
            System.out.println("Must specify connection string.");
            return;
        }

        if (collectionName == null) {
            System.out.println("Must specify collection name.");
            return;
        }

        create(connectionString, collectionName);
    }

    private static void create(String connectionString, String collectionName) {
        creator = new Creator(connectionString,collectionName);
        creator.importCSV("/Users/suhuruli/Downloads/"+collectionName+".csv");
    }
}
