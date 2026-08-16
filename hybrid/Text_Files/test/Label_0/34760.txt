import java.util.LinkedList;
import java.util.Scanner;

//Petoris
public class Main{

	class R{
		int h, w;
		LinkedList<LinkedList<Character>> p;
		public R(char[][] m) {
			p = new LinkedList<LinkedList<Character>>();
			for(int i=0;i<m.length;i++){
				LinkedList<Character> l = new LinkedList<Character>();
				for(int j=0;j<m[i].length;j++)l.add(m[i][j]);
				p.add(l);
			}
			for(;;){
				boolean f = true;
				for(char c:p.get(0))if(c=='#')f=false;
				if(!f)break;
				p.remove(0);
			}
			for(;;){
				boolean f = true;
				for(char c:p.get(p.size()-1))if(c=='#')f=false;
				if(!f)break;
				p.remove(p.size()-1);
			}
			h = p.size();
			for(;;){
				boolean f = true;
				for(int i=0;i<h;i++)if(p.get(i).get(0)=='#')f=false;
				if(!f)break;
				for(int i=0;i<h;i++)p.get(i).remove(0);
			}
			for(;;){
				boolean f = true;
				for(int i=0;i<h;i++)if(p.get(i).get(p.get(i).size()-1)=='#')f=false;
				if(!f)break;
				for(int i=0;i<h;i++)p.get(i).remove(p.get(i).size()-1);
			}
			w = p.get(0).size();
//			System.out.println("H:"+h+" W:"+w);
//			p(m);
		}
	}
	
	void p(char[][] a){
		for(int i=0;i<a.length;i++)System.out.println(new String(a[i]));
		System.out.println();
	}
	
	char[][] rot(char[][] a){
		int h = a.length, w = a[0].length;
		char[][] r = new char[w][h];
		for(int i=0;i<h;i++)for(int j=0;j<w;j++)r[j][i] = a[h-i-1][j];
		return r;
	}
	
	void run(){
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		while(T--!=0){
			int H = sc.nextInt(), W = sc.nextInt();
			R[] r = new R[4];
			char[][] p = new char[H][];
			for(int i=0;i<H;i++)p[i]=sc.next().toCharArray();
			for(int i=0;i<4;i++){
				r[i] = new R(p);
				p = rot(p);
			}
			H = sc.nextInt(); W = sc.nextInt();
			p = new char[H][];
			for(int i=0;i<H;i++)p[i]=sc.next().toCharArray();
			int res = -1;
			for(int k=0;k<4;k++){
				int h = r[k].h, w = r[k].w;
				for(int i=0;i+h<=H;i++)for(int j=0;j+w<=W;j++){
					boolean f = true;
					for(int y=0;y<h;y++)for(int x=0;x<w;x++){
						if(r[k].p.get(y).get(x)=='.')continue;
						if(p[i+y][j+x]=='#')f = false;
					}
					if(!f)continue;
					for(int y=0;y<h;y++)for(int x=0;x<w;x++){
						if(r[k].p.get(y).get(x)=='#')p[i+y][j+x] = '#';
					}
//					System.out.println("BEFORE:");
//					p(p);
					int c = 0;
					for(int y=0;y<h;y++){
						boolean ok = true;
						for(int x=0;x<W;x++)if(p[i+y][x]=='.')ok = false;
						if(ok)c++;
					}
					res = Math.max(res, c);
					for(int y=0;y<h;y++)for(int x=0;x<w;x++){
						if(r[k].p.get(y).get(x)=='#')p[i+y][j+x] = '.';
					}
//					System.out.println("AFTER:");
//					p(p);
				}
			}
			System.out.println(res);
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}