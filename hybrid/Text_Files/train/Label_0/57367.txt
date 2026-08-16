import java.util.*;
public class Main {
    public static void main(String[] args) {
        
      
        Scanner in = new Scanner(System.in);
        int result;
        String str1 = in.nextLine();
        String str2 = in.nextLine();
        //str1 = str1.toLowerCase();
       // str2 = str2.toLowerCase();
        result = str1.compareToIgnoreCase(str2);
        if(result == 0)
            System.out.println("0");
        else if(result!=0 && result <0)
            System.out.println("-1");
        else if(result!=0 && result > 0)
            System.out.println("1");
        
        
         
        
        
        }
        
            
        }