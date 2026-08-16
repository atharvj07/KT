
import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) {
		Scanner in=new Scanner(System.in);
		PrintWriter out=new PrintWriter(System.out);
		
		int n=Integer.parseInt(in.next()),q=Integer.parseInt(in.next());
		myqueue A[]=new myqueue[n];
		for(int i=0;i<n;i++)A[i]=new myqueue();
		
		for(int i=0;i<q;i++){
			int query=Integer.parseInt(in.next());
			
			switch(query){
			case 0:
				int t1=Integer.parseInt(in.next()),x=Integer.parseInt(in.next());
				A[t1].que.add(x);
				break;
				
			case 1:
				int t2=Integer.parseInt(in.next());
				if(!A[t2].que.isEmpty())out.println(A[t2].que.peek());
				break;
				
			case 2:
				int t3=Integer.parseInt(in.next());
				if(!A[t3].que.isEmpty())A[t3].que.remove();
				break;
			}
		}
		out.flush();
	}

}

class myqueue{
	Queue<Integer> que;
	
	myqueue(){
		que=new ArrayDeque<>();
	}
}

