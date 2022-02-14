package e201;

public enum DayOfWeek {
    Monday(true), Tuesday(true), Wednesday(true), Thursday(true), Friday(true), Saturday(false), Sunday(false);
    private boolean weekday;

    private DayOfWeek(boolean weekday) {
        this.weekday = weekday;
    }
    private boolean isWeekday() {
    return this.weekday;
    }

    @Override
    public String toString() {
        return name() + "(day " + (this.ordinal()+1) + ", weekday = " + this.weekday + ")";
    }
}

