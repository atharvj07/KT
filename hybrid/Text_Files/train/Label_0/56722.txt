import java.util.*;
import java.util.HashMap;
import java.util.Map.Entry;

public class Main{
    
    
    public static void main(String[] args) {

        ArrayList<ArrayList<String>> list = new ArrayList<ArrayList<String>>();
        
        Scanner sc = new Scanner(System.in);

        while(true){
            int N = Integer.parseInt(sc.nextLine());
            if(N == 0){
                break;
            }

            HashMap<String, String> henkan = new HashMap<String, String>();

            for(int i=0; i<N; i++){
                String line = sc.nextLine();
                String[] data = line.split(" ");
                henkan.put(data[0], data[1]); 
            }


            ArrayList<String> retu = new ArrayList<String>();
            int M = Integer.parseInt(sc.nextLine());
            for(int i=0; i<M; i++){
                String nyuryoku = sc.nextLine();
                if(henkan.containsKey(nyuryoku)){
                    retu.add(henkan.get(nyuryoku));
                }else{
                    retu.add(nyuryoku);
                }
                
            }
            list.add(retu);
        }
        
        
        for(int i=0; i<list.size(); i++){
            for(int k=0; k<list.get(i).size(); k++){
                System.out.print(list.get(i).get(k));
            }
            System.out.println();
        }

        /*System.out.println("HashMap--???????????????");
        int max = 0;
        
        for(Entry<Integer, Integer> entry : re.entrySet()){
                if(max < entry.getValue()){
                    max = entry.getValue();
                }
        }
        */
    }
}