package questions;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.util.List;

@Document(collection = "#{questionRepository.getCollectionName()}")
public class Questions {

    @Id
    public String id;

    public String questionID;
    public List<String> answers;
    public List<Integer> points;

    public Questions() {}


    @Override
    public String toString() {
        return "Customer[id=%s, firstName='%s', lastName='%s']";
    }

}