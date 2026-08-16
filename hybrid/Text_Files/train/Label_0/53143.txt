import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
            Scanner sc = new Scanner(System.in);
        
            int M = sc.nextInt();
            int D = sc.nextInt();
            
            int count = 0;
            
            for(int i = 1; i <= M; i++){
                for(int j = 22; j <= D; j++){
                    String dd = "" + j;
                    int x = Integer.parseInt(dd.substring(0,1));
                    int y = Integer.parseInt(dd.substring(1,2));
                    
                    if(i==x*y && y >= 2 && x >= 2){
                        count++;
                    }
                }   
            }
            System.out.println(count);
            
    }
}