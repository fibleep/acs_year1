package e202;

public class Movie {
    private String title;
    private int year;
    private Format format;
    private Audio audio;

    public Movie(String title, int year, Format format, Audio audio) {
        this.title = title;
        this.year = year;
        this.format = format;
        this.audio = audio;
    }

    @Override
    public String toString() {
        return String.format("%s %-6d %-3s %-3s", this.title, this.year, this.format, this.audio);
    }
}
