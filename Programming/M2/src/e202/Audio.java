package e202;

public enum Audio {
    PCM,DOLBY,DOLBY_HD,VHS,DTS_HD;

    @Override
    public String toString() {
        if(name().equals("DOLBY")){
            return "Dolby";
        }
        else if(name().equals("DOLBY_HD")){
            return "Dolby HD";
        }
        else if(name().equals("DTS_HD")){
            return "DTS HD";
        }
        else{
            return name();
        }
    }
}
