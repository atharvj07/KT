
import java.util.*;
import java.io.*;

class Main {
	public static void main(String[] args){
		new Main().new P1127().run(); 
	}
	class P1127{
		void run(){
			Scanner sc=new Scanner(System.in);
			for(;;){
				int n=sc.nextInt();
				if(n==0)break;
				
				Pos[] p=new Pos[n];
				Queue<Node> q=new PriorityQueue<Node>();
				boolean[] visited=new boolean[n];
				int nvis=0;
				double ans=0;
				
				for(int i=0;i<n;i++){
					double x,y,z,r;
					x=sc.nextDouble();
					y=sc.nextDouble();
					z=sc.nextDouble();
					r=sc.nextDouble();
					p[i]=new Pos(x,y,z,r);
					visited[i]=false;
				}
				
				//Prim
				Node t=new Node(0,0);
				q.offer(t);
				while(nvis<n){
					t=q.poll();
					if(visited[t.node])continue;
					visited[t.node]=true;
					nvis++;
					ans+=t.d;
					for(int i=0;i<n;i++){
						if(!visited[i]){
							q.offer(new Node((p[t.node]).dist(p[i]),i));
						}
					}
				}
				System.out.printf("%.3f\n",ans);
			}
		}
	}
	class Pos{
		double x,y,z,r;
		Pos(double x_,double y_,double z_,double r_){
			this.x=x_;
			this.y=y_;
			this.z=z_;
			this.r=r_;
		}
		double dist(Pos o){
			double ret=Math.sqrt((x-o.x)*(x-o.x)+(y-o.y)*(y-o.y)+(z-o.z)*(z-o.z))-(r+o.r);
			return ret<=0?0:ret;
		}
	}
	class Node implements Comparable<Node>{
		double d;
		int node;
		public int compareTo(Node o){
			if(d<o.d)return -1;
			if(d==o.d)return 0;
			else return 1;
		}
		Node(double d_,int node_){
			this.d=d_;
			this.node=node_;
		}
	}
}