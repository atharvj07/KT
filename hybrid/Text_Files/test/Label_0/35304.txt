import java.util.*;
import java.lang.*;
import java.io.*;

class Main{


      public static void main(String args[])throws IOException{
	  BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	  while(true)
	      {
		  String line = in.readLine();
		  int n,m;
		  n = Integer.parseInt(line.substring(0,line.indexOf(" ")));
		  m = Integer.parseInt(line.substring(line.indexOf(" ")+1));
		  if(n+m == 0)break;
		  String[] elements = in.readLine().split(" ");
		  
		  HashMap<String,Integer> index = new HashMap<String,Integer>();
		  index.put(elements[0],0);
		  index.put(elements[1],1);
		  index.put(elements[2],2);
		  int pos = 3;	      
		  int[][] imap = new int[n][n];
		  for(int i=0;i<n;i++)
		      for(int j=0;j<n;j++)
			  imap[i][j] = 10000000;

		  for(int i=0;i<m;i++)
		      {
			  String[] input = in.readLine().split(" ");

			  if(!index.containsKey(input[0]))
			      {
				  index.put(input[0],pos);
				  pos++;
			      }

			  if(!index.containsKey(input[1]))
			      {
				  index.put(input[1],pos);
				  pos++;
			      }

			  int d,t;
			  d = Integer.parseInt(input[2]);
			  t = Integer.parseInt(input[3]);

			  int cost = d/40 + t;

			  imap[index.get(input[0])][index.get(input[1])] = imap[index.get(input[1])][index.get(input[0])] = cost;

		      }

		  for(int k=0;k<n;k++)
		      for(int i=0;i<n;i++)
			  for(int j=0;j<n;j++)
			      imap[i][j] = Math.min(imap[i][j],imap[i][k] + imap[k][j]);

		  System.out.println(imap[index.get(elements[0])][index.get(elements[1])] + imap[index.get(elements[1])][index.get(elements[2])]);

	      }
      }

}