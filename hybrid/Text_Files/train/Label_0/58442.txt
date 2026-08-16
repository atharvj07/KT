import java.util.*;

/**
 *
 *
 *  @author Mustafa Arinmis
 *  @since 05.11.2020
 * */

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int m = input.nextInt();
        TreeMap<Integer, Integer> containers = new TreeMap<>(Collections.reverseOrder());

        int key, value;
        for(int i=0; i<m; i++) {
            value = input.nextInt();
            key = input.nextInt();

            if(containers.containsKey(key))
                containers.put(key , value + containers.get(key));
            else
                containers.put(key , value);
        }



        int maxMatch = 0;
        for(Map.Entry entry : containers.entrySet()){
            if(n > (Integer)entry.getValue()) {
                maxMatch += (Integer) entry.getKey() * (Integer) entry.getValue();
                n -= (Integer) entry.getValue();
            }
            else{
                maxMatch += n *  (Integer) entry.getKey();
                break;
            }
        }

        System.out.println(maxMatch);

    }
}

