
import java.util.Scanner;

/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Ahmad
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner input=new Scanner(System.in);
        int k;
        String str;
        str=input.nextLine();
        k=input.nextInt();
        int len=str.length();
        if(len <=k){
            System.out.printf("%d\n",  (len+k)%2==1 ? len+k-1: len+k);
        }else{
             int ans = 0;
             for (int i = 0; i < len; i++) 
             {
                 for (int j = i+1; 2*j-i <= len+k; j++)
                 {
                     boolean ok = true;
                     for (int l = 0; l < j-i && l+j < len; l++)  
                     {
                         if (str.charAt(i+l) != str.charAt(j+l))
                         {
                             ok = false;
                             break;
                         }
                     }
                     if (!ok)
                         continue;
                     ans = Math.max(ans, 2*(j-i));
                 }
             }
             System.out.printf("%d\n", ans);
        }
     
    }
}
