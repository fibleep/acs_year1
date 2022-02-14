package e202;

public enum Format {
    VHS,DVD,BLU_RAY;

    @Override
    public String toString() {
        if (name().equals("BLU_RAY")){
            return "Blu-ray";
        }
        else{
            return name();
        }
    }
}
