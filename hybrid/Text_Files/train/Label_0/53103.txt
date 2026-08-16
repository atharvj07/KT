import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class cf {
    public static void main(String[] args) throws Exception {
        Scanner in=new Scanner(System.in);
        int n=in.nextInt();
        int max=in.nextInt();
        int pre=max;
        int pos,tem;
        int energ=0;
        for(int i=0;i<n-1;i++)
        {
        	pos=in.nextInt();
        	tem=pre-pos;
        	if(energ+tem<0)
        	{
        		max+=Math.abs(energ+tem);
        		energ=0;
        	}
        	else
        		energ+=tem;
        	pre=pos;
        }
        System.out.println(max);
    }
}