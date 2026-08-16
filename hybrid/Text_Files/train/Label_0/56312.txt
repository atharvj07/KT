import java.util.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int H = sc.nextInt();
        int W = sc.nextInt();
        String [][] s = new String[H+2][W+2];

        for(int i = 0 ; i <= (H+1) ; i++){
        	for(int j = 0 ; j <= (W+1) ; j++){
        		s[i][j] = " ";
        	}
        }
        
        String kekka = "Yes";

        for(int i = 1 ; i <= H  ; i++){
            String[] str = sc.next().split("");
            for(int j = 1 ; j <= W ; j++){
                s[i][j] = str[j-1];
            }
        }

        for(int i = 1 ; i <= H  ; i++){
            for(int j = 1 ; j <= W ; j++){
                if(s[i][j].equals("#")){
                	if((s[i-1][j].equals(".")) && (s[i][j-1].equals(".")) && (s[i][j+1].equals(".")) && (s[i+1][j].equals("."))){
                		kekka = "No";
                		break;
                	}
                }
            }
        }

        System.out.println(kekka);
    }
}