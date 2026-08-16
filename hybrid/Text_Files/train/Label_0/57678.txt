import java.util.Scanner;

public class Welcomejava { 
      
    public static void main(String[] args) {
        // TODO code application 
        Scanner input = new Scanner(System.in);
        int t ;
        t = input.nextInt();
        while (t-->0) {
            String s ;
            s = input.next();
            char[] arr = new char[s.length()];
            for (int i = 0; i < s.length() ; i++) {
                arr[i] = s.charAt(i);
            }
            boolean flage = false;
            for (int i = 0; i < arr.length; i++) {
                
                if (flage == false)
                {
                 if (arr[i] == 'a')
                 {
                  arr[i] = 'b';
                  flage = true;
                 }
                 else
                 {
                  arr[i] = 'a';
                  flage = true;
                 }
                }
                else
                {
                if (arr[i] == 'z')
                {
                arr[i] = 'y';
                flage = false;
                }
                else
                {
                 arr[i] = 'z';
                 flage = false;
                }
                 
                }
            }
         for(char c : arr)
         {
             System.out.print(c);
         }
            System.out.println("");
        }
    }
}

