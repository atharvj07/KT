/* 
Link of Question : http://codeforces.com/problemset/problem/259/A
*/

import java.util.Scanner;

public class LittleElephantAndChess {

   
    public static void main(String[] args) 
    {
        Scanner in=new Scanner(System.in);
        boolean flag=true;
        for (int i = 0; i < 8; i++) 
        {
            String S=in.next();
            if (S.contains("WW")||S.contains("BB"))
            {
                flag=false;
            }
            
        }
        
        if (flag)
        {
            System.out.println("YES");
        }
        else
        {
            System.out.println("NO");
        }
       
    }
    
}
