import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


public class Solution {
	public static void main(String[] args) {
        
        Scanner in = new Scanner(System.in);   
        
        int n = in.nextInt();
        
        if(n%2==0)
        {
            System.out.println(n/2);
            for(int i=0; i<n/2; i++)
                System.out.print(2+" ");
        }
        else
        {
            System.out.println(n/2);
            for(int i=0; i<(n/2)-1; i++)
                System.out.print(2+" ");
            System.out.print(3+" ");
        }  
        
	}
}