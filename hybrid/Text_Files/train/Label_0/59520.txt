import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int[] science = new int[4];
        int[] sciety = new int[2];

        for(int i=0;i<6;i++){
            if(i<4) science[i] = sc.nextInt();
            else sciety[i-4] = sc.nextInt();        
        }

        for(int i=0;i<4;i++){
            for(int j=i+1;j<4;j++){
                if(science[i]>science[j]){
                    int x = science[i];
                    science[i] = science[j];
                    science[j] = x;
                }
            }
        }
        if(sciety[0]>sciety[1]){
            int y = sciety[0];
            sciety[0] = sciety[1];
            sciety[1] = y;
        }
        System.out.println(science[1]+science[2]+science[3]+sciety[1]);
    }
}
