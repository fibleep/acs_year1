package e102;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

public class e102 {
    public static void main(String[] args) {
        List<Integer> numberList = new ArrayList<>();
        Random rand = new Random();
        for (int i = 0; i <= 20; i++) {
            numberList.add(rand.nextInt(1,51));
        }
        System.out.println(numberList);
        Integer[] arr = numberList.toArray(new Integer[0]);
        for (Integer integer : arr) {
            System.out.println(integer);
        }
        List<Integer> evenNumbers = new ArrayList<>(numberList);
        for (int i = 0; i < evenNumbers.size(); i++) {
            int x = evenNumbers.get(i);
            if(x%2!=0){
                evenNumbers.remove(i);
                i--;
            }
        }
        System.out.println(evenNumbers);
        System.out.println("\n\n e105");
        Collections.sort(numberList);
        System.out.println(numberList);
        Collections.reverse(numberList);
        System.out.println(numberList);
        Collections.shuffle(numberList);
        System.out.println(numberList);
        System.out.println(Collections.frequency(numberList,48));
    }
}
