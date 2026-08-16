import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Scanner;

//Online Quiz System
public class Main{

	int WORK = 0, START = 1, END = 2, SUBMIT = 3;
	
	class E implements Comparable<E>{
		int type, t, id;
		public E(int type, int t, int id) {
			this.type = type;
			this.t = t;
			this.id = id;
		}
		public int compareTo(E o) {
			return t!=o.t?t-o.t:type-o.type;
		}
	}
	
	void run(){
		Scanner sc = new Scanner(System.in);
		boolean[] just = new boolean[100], sub = new boolean[100];
		int[] L = new int[100], send = new int[100], rev = new int[100], delay = new int[100];
		for(boolean H=true;;H=false){
			int M = sc.nextInt(), N = sc.nextInt();
			if((M|N)==0)break;
			if(!H)System.out.println();
			Arrays.fill(send, 0); Arrays.fill(rev, 0);
			for(int i=0;i<M;i++)delay[i]=sc.nextInt();
			while(N--!=0){
				Arrays.fill(L, 0); Arrays.fill(just, false); Arrays.fill(sub, false);
				PriorityQueue<E> q = new PriorityQueue<E>();
				q.add(new E(START, 0, -1)); q.add(new E(END, 20000, -1));
				for(int t=1000;t<=20000;t+=1000)q.add(new E(WORK, t, -1));
				int k = sc.nextInt();
				while(k--!=0){
					int id = sc.nextInt(), t = sc.nextInt(), len = sc.next().length();
					q.add(new E(SUBMIT, t+delay[id]*2, id));
					L[id] = len;
				}
				while(!q.isEmpty()){
					E e = q.poll();
					if(e.type==START){
						for(int i=0;i<M;i++)rev[i]+=3;
					}
					else if(e.type==END){
						for(int i=0;i<M;i++)rev[i]+=4; break;
					}
					else if(e.type==SUBMIT){
						just[e.id] = sub[e.id] = true;
						send[e.id] += 5+L[e.id];
					}
					else{
						int newly = 0, submit = 0, allsize = 0, newlysize = 0;
						for(int i=0;i<M;i++){
							if(just[i])newly++;
							if(just[i])newlysize+=L[i];
							if(sub[i])submit++;
							if(sub[i])allsize+=L[i];
						}
						for(int i=0;i<M;i++){
							if(!sub[i]){
								if(0<newly){
									rev[i]+=4+newly;
								}
							}
							else if(just[i]){
								if(1<submit){
									rev[i]+=4+2*(submit-1)+allsize-L[i];
								}
							}
							else{
								if(0<newly){
									rev[i]+=4+2*newly+newlysize;
								}
							}
						}
						Arrays.fill(just, false);
					}
				}
			}
			int ress = 0, resr = 0;
			for(int i=0;i<M;i++){
				ress+=rev[i]; resr+=send[i];
			}
			System.out.println(ress+" "+resr);
			for(int i=0;i<M;i++)System.out.println(send[i]+" "+rev[i]);
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}