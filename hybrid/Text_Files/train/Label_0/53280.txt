import java.util.*;


public class C163 {
	
	class Line{
		public ArrayList<Integer> l = new ArrayList<Integer>();
		public int yuan;

		public Line() {
			l = new ArrayList<Integer>();
		}
		
		
	}
	
	class Lie{
		public int min;
		public int shu;
		public int yuan;
		public Lie(int min, int shu, int yuan) {
			super();
			this.min = min;
			this.shu = shu;
			this.yuan = yuan;
		}
		
		
	}
	
	class Jl{
		public int a,b,c;

		public Jl(int a, int b, int c) {
			super();
			this.a = a;
			this.b = b;
			this.c = c;
		}

		@Override
		public String toString() {
			return String.format("%d %d %d", a,b,c);
		}
		
	}
	
	Line maz[] ;
	Lie lie[];
	int juzhen[][];
	
	List <Jl> ans = new LinkedList<Jl>();
	
	void run(){
		
		Scanner cin = new Scanner(System.in);
		int n = cin.nextInt();
		maz = new Line[n+1];
		
		int i,j;
		for(i=0;i<n+1;i++){
			maz[i] = new Line();
			maz[i].yuan = i;
		}
		maz[0].yuan = 0;
		for(i=0;i<n-1;i++){
			int x = cin.nextInt();
			int y = cin.nextInt();
			maz[x].l.add(y);
		}
		
		Arrays.sort(maz,new Comparator<Line>() {

			@Override
			public int compare(Line o1, Line o2) {
				if(o1.l.size() != o2.l.size())
					return o1.l.size() - o2.l.size();
				return o1.yuan - o2.yuan;
			}
			
		});
		
		int bi[] = new int[n+1];
		
		for(i=0;i<=n;i++)
			bi[maz[i].yuan] = i;
		for(i=n;i>=1;i--){
			if(i != bi[i])
			{
				int w = i;
				for(j=1;j<=n;j++)
				{
					if(bi[j] == i)
						w = j;
				}
				ans.add(new Jl(1,i,w));
				int temp = bi[i];
				bi[i] = bi[w];
				bi[w] = temp;
			}
		}
		
		
		
		
		juzhen = new int[n+1][n+1];
		for(i=1;i<=n;i++){
			for(j=1;j<=n;j++)
				juzhen[i][j] = 0;
		}
		for(i=n;i>=1;i--){
			if(maz[i].l.size() == 0)
				break;
			for(j=0;j<maz[i].l.size();j++)
			{
				juzhen[i][maz[i].l.get(j)] = 1;
			}
		}
		
		lie = new Lie[n+1];
		
		lie[0] = new Lie(-9,90000,-9);
		
		for(j=1;j<=n;j++){
			
			boolean flag = false;
			int count = 0;
			int min = -1;
			for(i=1;i<=n;i++){
				if(juzhen[i][j] == 1 && flag == false)
				{
					flag =true;
					min = i;
					count ++;
				}
				else if(juzhen[i][j] == 1){
					count ++;
				}
			}
			lie[j] = new Lie(min, count,j);
		}
		
		Arrays.sort(lie,new Comparator<Lie>() {

			@Override
			public int compare(Lie o1, Lie o2) {
				
				if(o1.shu != o2.shu)
				{
					return o2.shu - o1.shu;
				}
				return o1.min - o2.min;
			}
			
		});
		
		
		for(i=1;i<=n;i++)
			bi[lie[i].yuan] = i;
		
		for(i=n;i>=1;i--){
			if(i != bi[i])
			{
				int w = i;
				for(j=1;j<=n;j++)
				{
					if(bi[j] == i)
						w = j;
				}
				ans.add(new Jl(2,i,w));
				int temp = bi[i];
				bi[i] = bi[w];
				bi[w] = temp;
			}
		}
		
		System.out.println(ans.size());
		for(Jl buf : ans){
			System.out.println(buf);
		}
	}
	
	
	
	
	public static void main(String[] args) {
		
		new C163().run();
	}
}
