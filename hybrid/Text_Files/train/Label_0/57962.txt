import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.io.StreamTokenizer;

import javax.swing.JInternalFrame;
 
public class Main
{
    public static void main(String[] args) throws IOException
    {
    	StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));		
		PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));
		in.nextToken();
        int num = (int)in.nval;
        //两行，第一行存储是否送出礼物，0否，其他数字，送给的人：送给的人；第二行存储是否收到礼物，0否1是
        int[][] numLine = new int[num + 1][2];
        
        for(int i = 1; i <= num; i++)
        {
        	in.nextToken();
        	int num1 = (int)in.nval;
        	if(num1 != 0)
        	{
        		numLine[i][0] = num1;
        		numLine[num1][1] = 1;
        	}
        }
        int allLost = 0;
        for(int i = 1; i <= num; i++)
        {
        	if(numLine[i][0] == 0)
        	{
        		allLost++;
        	}
        }
        int i1 = 1;
        int i2 = 1;
        int[][] tempLine = new int[2][4];
        if(allLost % 2 == 1)
        {
        	for(;tempLine[0][0] != 3;i1++)
        	{
        		
        		if(numLine[i1][0] == 0)
        		{
        			tempLine[0][tempLine[0][0] + 1] = i1;
        			tempLine[0][0] += 1;
        		}
        		
        	}
        	for(;tempLine[1][0] != 3;i2++)
        	{
        		if(numLine[i2][1] == 0)
        		{
        			tempLine[1][tempLine[1][0] + 1] = i2;
        			tempLine[1][0] += 1;
        		}
        	}
        	for(;;)
        	{
        		if(tempLine[0][1] != tempLine[1][1] && tempLine[0][2] != tempLine[1][2] && tempLine[0][3] != tempLine[1][3])
            	{
        			for(int j = 1; j < 4; j++)
            		{
            			numLine[tempLine[0][j]][0] = tempLine[1][j];
            		}
            		tempLine[0][0] = 0;
            		tempLine[1][0] = 0;
            		break;
            	}
            	else 
            	{
        			int t1 = tempLine[1][1];
        			tempLine[1][1] = tempLine[1][2];
        			tempLine[1][2] = tempLine[1][3];
        			tempLine[1][3] = t1;
            	}
        	}
        }
        
        for(; i1 <= num || i2 <= num;)
        {
        	for(;tempLine[0][0] != 2 && i1 <= num;i1++)
        	{
        		
        		if(numLine[i1][0] == 0)
        		{
        			tempLine[0][tempLine[0][0] + 1] = i1;
        			tempLine[0][0] += 1;
        		}
        		
        	}
        	for(;tempLine[1][0] != 2 && i2 <= num;i2++)
        	{
        		if(numLine[i2][1] == 0)
        		{
        			tempLine[1][tempLine[1][0] + 1] = i2;
        			tempLine[1][0] += 1;
        		}
        	}
        	for(;;)
        	{
        		if(tempLine[0][1] != tempLine[1][1] && tempLine[0][2] != tempLine[1][2])
            	{
        			for(int j = 1; j < 3; j++)
            		{
            			numLine[tempLine[0][j]][0] = tempLine[1][j];
            		}
            		tempLine[0][0] = 0;
            		tempLine[1][0] = 0;
            		break;
            	}
            	else 
            	{
        			int t1 = tempLine[1][1];
        			tempLine[1][1] = tempLine[1][2];
        			tempLine[1][2] = t1;
            	}
        	}
        }
        for(int i = 1; i <= num; i++)
        {
        	if(i != 1)
        	{
        		System.out.print(" ");
        	}
        	System.out.print(numLine[i][0]);
        }
        
        
    }
}