import java.util.HashMap;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        HashMap<String,Long> namelist = new HashMap<>();
        String s = "MARCH";
        for(int i = 0;i<s.length();i++){
            namelist.put(String.valueOf(s.charAt(i)), Long.valueOf(0));
        }
        for (int i = 0; i < n; i++) {
            String name = String.valueOf(sc.next().charAt(0));
            if(namelist.containsKey(name)){
                namelist.put(name,namelist.get(name)+1);
            }
        }
        
        long ans=0;
        
        for(int i =0;i<s.length()-2;i++){
            long a = namelist.get(String.valueOf(s.charAt(i)));
            for(int j=i+1;j<s.length()-1;j++){
                long b = namelist.get(String.valueOf(s.charAt(j)));
                for(int k = j+1;k<s.length();k++){
                    long c = namelist.get(String.valueOf(s.charAt(k)));
                    ans += a*b*c;
                }
            }
        }
        System.out.println(ans);
    }
}