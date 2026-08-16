import java.util.ArrayList;
import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        String F = sc.next();
        String M = sc.next();
        String S = sc.next();
    
        //if (!F.equals(M) && !F.equals(S) && !M.equals(S)){System.out.println("?");}
        if (F.equals("paper") && M.equals("rock") && S.equals("rock")){System.out.println("F");}
        else if (F.equals("rock") && M.equals("paper") && S.equals("rock")){System.out.println("M");}
        else if (F.equals("rock") && M.equals("rock") && S.equals("paper")){System.out.println("S");}
        
        else if (F.equals("scissors") && M.equals("paper") && S.equals("paper")){System.out.println("F");}
        else if (F.equals("paper") && M.equals("scissors") && S.equals("paper")){System.out.println("M");}
        else if (F.equals("paper") && M.equals("paper") && S.equals("scissors")){System.out.println("S");}
        
        else if (F.equals("rock") && M.equals("scissors") && S.equals("scissors")){System.out.println("F");}
        else if (F.equals("scissors") && M.equals("rock") && S.equals("scissors")){System.out.println("M");}
        else if (F.equals("scissors") && M.equals("scissors") && S.equals("rock")){System.out.println("S");}
        else System.out.println("?");
    }   
}