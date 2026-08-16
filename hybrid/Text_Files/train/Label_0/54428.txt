import java.util.*;
import java.lang.*;
import java.io.*;
import java.awt.Point;

class Main{

    public static class Pox{
	public int id,time,difficulty;
	Pox(){
	    id = time = difficulty = 0;
	}

	Pox(int a,int b,int c){
	    id = a;
	    time = b;
	    difficulty = c;
	}

    }

    public static void main(String args[])throws IOException{
	BufferedReader in = new BufferedReader(new InputStreamReader(System.in));  
	while(true)
	      {
		  int n,m;
		  String line = in.readLine();
		
		  List<Integer> list = new ArrayList<Integer>();
		  List<Integer> list2 = new ArrayList<Integer>();

		  n = Integer.parseInt(line.substring(0,line.indexOf(" ")));
		  m = Integer.parseInt(line.substring(line.indexOf(" ")+1));
		  
		  if(n == 0 && m == 0)
		      break;		  

		  String[] elements = in.readLine().split(" ");    

		  for(int i=0;i<elements.length;i++)
		      {
			  list.add(Integer.parseInt(elements[i]));
		      }

		  int pre = m;
		  List<Pox> list3 = new ArrayList<Pox>();

		  for(int i=0;i<list.size();i++)
		      {
			
			  if(pre >= m/list.get(i)*list.get(i))
			      {
				  list2.add(m/list.get(i)*list.get(i));
				  pre = m/list.get(i)*list.get(i);
				  list3.add(new Pox(i,pre,list.get(i)));
			      }
			  else
			      {
				  int val = list.get(i);
				  int cnt = val;
				  while(val*cnt < pre)
				      {
					  cnt++;
				      }
			
				  list2.add(val*cnt);
				  pre = val*cnt;
				  list3.add(new Pox(i,pre,val));
			      }
			 
		      }

		  Collections.sort(list3,new Comparator<Pox>(){

			  @Override
			      public int compare(Pox a,Pox b){
			      if(a.time != b.time)
				  {
				      if(a.time > b.time)
					  return 1;
				      else 
					  return -1;
				  }
			      if(a.difficulty != b.difficulty)
				  {
				      if(a.difficulty > b.difficulty)
					  return 1;
				      else
					  return -1;
				  }
			      return -1;
			  }
		      });

		  if(list3.get(0).time != list3.get(1).time)
		      {
			  System.out.println(list3.get(0).id+1);
		      }
		  else if(list3.get(0).difficulty != list3.get(1).difficulty)
		      {
			  System.out.println(list3.get(0).id+1);
		      }
		  else
		      {
			  System.out.println(n);
		      }


	      }
      }

}