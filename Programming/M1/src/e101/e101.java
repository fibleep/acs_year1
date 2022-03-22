package e101;

import java.util.ArrayList;
import java.util.List;

public class e101 {
    public static void main(String[] args) {
        List<String> myList = new ArrayList<>();
        String[] names = {"Albert","Henry","Josephine","Annabelle","Asgraf"};
        for (int i = 0; i < names.length; i++) {
            myList.add(names[i]);
        }
        System.out.println("First: " + myList.get(0));
        System.out.println("Last: " + myList.get(myList.size()-1));
        System.out.println("\nprintin shtuff");
        for (String name: myList
             ) {
            System.out.println(name);
        }

        System.out.println(isGeorgie(myList));
        for (int i = 0; i < myList.size(); i++) {
            if (myList.get(i).startsWith("A")){
                myList.remove(i);
                i--;
            }
        }
        System.out.println(myList);
    }
    public static boolean isGeorgie(List<String> list){
        for (String name:list
             ) {
            if(name=="Georgie"){
                return true;
            }
        }
        return false;
    }

}
