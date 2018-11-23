package questions;

public class QuestionRepositoryImpl implements QuestionRepositoryCustom {

    private static String collectionName = "3-answers";

    @Override
    public String getCollectionName() {
        return collectionName;
    }

    @Override
    public void setCollectionName(String collectionName) {
        this.collectionName = collectionName;
    }
}
