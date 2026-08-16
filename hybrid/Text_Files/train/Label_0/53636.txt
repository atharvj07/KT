import java.util.Scanner;
import java.util.HashMap;

class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        HashMap<String,Integer> map = new HashMap<String,Integer>();

        int n = sc.nextInt();
        for(int i = 0; i < n; i++){
            String s = sc.next();
            if(map.containsKey(s)){
                map.replace(s, map.get(s)+1);
            }else{
                map.put(s,1);
            }
        }

        int m = sc.nextInt();
        for(int i = 0; i < m; i++){
            String s = sc.next();
            if(map.containsKey(s)){
                map.replace(s, map.get(s)-1);
            }
        }

        int result = 0;
        for(Integer fuga : map.values()){
            if(fuga > result){
                result = fuga;
            }
        }

        System.out.println(result);
    }
}