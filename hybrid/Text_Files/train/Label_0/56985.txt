/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
public class Trees
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner scan = new Scanner(System.in);
		int numTrees = scan.nextInt();
		int ans = 0;
		int[] positions = new int[numTrees];
		int[] heights = new int[numTrees];
		
		if(numTrees == 1)
			ans = 1;
		else
		{
			if(numTrees > 1) ans = 2; //if there are at least two trees, we can at least fell them in opposite directions
			for(int i = 0; i < numTrees; i++)
			{
				positions[i] = scan.nextInt();
				heights[i] = scan.nextInt();
			}
			for(int j = 1; j < numTrees-1; j++)
			{
				//System.out.println("right? " + positions[j] + "+" + heights[j] + "<?" + positions[j+1]);
				if(positions[j] - heights[j] > positions[j-1])
				{
					ans++;
					// System.out.println("fell tree " + j + " of height " + heights[j] + " to the left");
				}
				else if(positions[j] + heights[j] < positions[j+1])
				{
					ans++;
					// System.out.println("fell tree " + j + " of height " + heights[j] + " to the right");
					positions[j] += heights[j];
				}
				
			}
		}
		
		System.out.println(ans);
	}
}