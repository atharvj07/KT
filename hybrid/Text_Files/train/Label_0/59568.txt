import java.util.PriorityQueue;
import java.util.Scanner;

//Data Center on Fire
public class Main{

	final int NONE = 0, GO = 1, GET = 2, BACK = 3, FIRE = 4, RELEASE = 5;
	class E{
		int id, cap, stop, c, state, tar;
		double pos, v;
		public E(int id, int cap, int stop, double pos, double v) {
			this.id = id;
			this.cap = cap;
			this.stop = stop;
			this.pos = pos;
			this.v = v;
		}
	}
	class R implements Comparable<R>{
		int event, p;
		double t;
		public R(int event, int p, double t) {
			this.event = event;
			this.p = p;
			this.t = t;
		}
		public int compareTo(R o) {
			return (int)Math.signum(t-o.t);
		}
	}

	int N, M, target;
	double[] fh;
	int[] dev;
	E[] es;
	boolean ex;

	void next(){
		while(target>0&&dev[target]==0)target--;
	}
	boolean con(){
		if(target>1)return true;
		for(int i=0;i<M;i++)if(es[i].state!=NONE)return true;
		return false;
	}

	void run(){
		Scanner sc = new Scanner(System.in);
		for(;;){
			N = sc.nextInt(); M = sc.nextInt();
			if((N|M)==0)break;
			target = N; ex = false;
			int H = sc.nextInt();
			fh = new double[N+1];
			for(int i=1;i<=N;i++)fh[i]=(i-1)*H;
			dev = new int[N+1];
			for(int i=1;i<=N;i++)dev[i]=sc.nextInt();
			next();
			es = new E[M];
			for(int i=0;i<M;i++){
				int c = sc.nextInt(), v = sc.nextInt(), stop = sc.nextInt(), x = sc.nextInt();
				es[i] = new E(i, c, stop, fh[x], v);
			}
			PriorityQueue<R> q = new PriorityQueue<R>();
			int[] fire = new int[N+1];
			int K = sc.nextInt(), tf = sc.nextInt(), tup = sc.nextInt(), tdn = sc.nextInt();
			for(int i=K-1;i>0;i--)fire[i]=fire[i+1]+tdn;
			for(int i=K+1;i<=N;i++)fire[i]=fire[i-1]+tup;
			for(int i=1;i<=N;i++)q.add(new R(FIRE, i, fire[i]+tf));
			for(int i=0;i<M;i++){
				if(target==1)es[i].state = NONE;
				else{
					es[i].state = GO; es[i].tar = target;
				}
			}
			
			int res = dev[1];
			dev[1] = 0;
			double t = 0, anst = 0;
			while(con()){
				int id = -1;
				double min = 1<<29;
				for(int i=0;i<M;i++){
					if(es[i].state!=GO)continue;
					double dt = t + Math.abs(fh[es[i].tar]-es[i].pos)/es[i].v;
					if(dt<min){
						min = dt; id = i;
					}
				}
				if(id!=-1&&(q.isEmpty()||!q.isEmpty()&&min<q.peek().t)){
//					System.out.println("Reach:"+id+" on:"+es[id].tar+" dev:"+dev[es[id].tar]+" at:"+min);
					double dt = min-t;
					for(int i=0;i<M;i++){
						if(es[i].state!=GO)continue;
						if(fh[es[i].tar]<es[i].pos)es[i].pos-=es[i].v*dt;
						else es[i].pos+=es[i].v*dt;
					}
					int carry = Math.min(dev[es[id].tar], es[id].cap-es[id].c);
					es[id].c += carry;
					es[id].state = GET;
					q.add(new R(GET, id, min+es[id].stop));
					dev[es[id].tar] -= carry;
					if(es[id].tar>1)ex = true;
//					System.out.println("Ev:"+id+" "+es[id].c+"/"+es[id].cap+" Floor rest:"+dev[es[id].tar]+" Pos:"+es[id].pos);
					if(dev[es[id].tar]==0){
						next();
						if(target>1){
							for(int i=0;i<M;i++){
								if(es[i].state!=GO)continue;
								es[i].tar = target;
							}
						}
						else{
							for(int i=0;i<M;i++){
								if(es[i].state!=GO)continue;
								if(es[i].c==0)es[i].state = NONE;
								else {
									es[i].state = BACK;
									q.add(new R(BACK, i, min+es[i].pos/es[i].v));
								}
							}
						}
					}
					t = min;
				}
				else{
					R r = q.poll();
					double dt = r.t-t;
					for(int i=0;i<M;i++){
						if(es[i].state!=GO)continue;
						if(fh[es[i].tar]<es[i].pos)es[i].pos-=es[i].v*dt;
						else es[i].pos+=es[i].v*dt;
					}
					if(r.event==GET){
//						System.out.println("Close :"+r.p+" at:"+r.t);
//						if(es[r.p].tar==1){
//							anst = r.t;
//							if(target>0){
//								es[r.p].state = GO;
//								es[r.p].tar = target;
//							}
//							else es[r.p].state = NONE;
//						}
//						else{
							if(es[r.p].c==es[r.p].cap){
								es[r.p].state = BACK;
								es[r.p].tar = 1;
								q.add(new R(BACK, r.p, r.t+es[r.p].pos/es[r.p].v));
							}
							else{
								if(target>1){
									es[r.p].state = GO; es[r.p].tar = target;
								}
								else{
									es[r.p].state = BACK;
									es[r.p].tar = 1;
									q.add(new R(BACK, r.p, r.t+es[r.p].pos/es[r.p].v));
								}
							}
//						}
					}
					else if(r.event==BACK){
//						System.out.println("Back: "+r.p+" at:"+r.t+" with:"+es[r.p].c);
						es[r.p].pos = 0;
						es[r.p].state = RELEASE;
						q.add(new R(RELEASE, r.p, r.t+es[r.p].stop));
					}
					else if(r.event==RELEASE){
						anst = r.t;
						res += es[r.p].c; es[r.p].c = 0;
						if(target>1){
							es[r.p].state = GO; es[r.p].tar = target;
						}
						else es[r.p].state = NONE;
					}
					else if(r.event==FIRE){
//						System.out.println("Fire on:"+r.p+" at:"+r.t);
						dev[r.p] = 0;
						next();
						for(int i=0;i<M;i++){
							if(es[i].state!=GO)continue;
							if(target>1)es[i].tar = target;
							else{
								if(es[i].c==0)es[i].state=NONE;
								else{
									es[i].state = BACK; es[i].tar = 1;
									q.add(new R(BACK, i, r.t+es[i].pos/es[i].v));
								}
							}
						}
					}
					t = r.t;
				}
			}
			System.out.printf("%d %.6f\n", res, ex?anst:0);
		}
	}

	public static void main(String[] args) {
		new Main().run();
	}
}