package e103;

import java.util.ArrayList;
import java.util.List;

public class Menu {
    List<Drink> menu = new ArrayList<Drink>();
    public void addDrink(Drink drink){
        menu.add(drink);
    }
}
