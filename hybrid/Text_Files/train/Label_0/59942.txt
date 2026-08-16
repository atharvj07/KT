import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

//Pathological Paths
public class Main{

	class F{
		int id;
		String name;
		public F(int id, String name) {
			this.id = id;
			this.name = name;
//			System.out.println("Make file:" + name + " ID:" + id);
		}
	}
	
	class D{
		String name;
		D parent;
		List<D> dir;
		List<F> file;
		public D(String name, D parent) {
			this.name = name;
			this.parent = parent;
			dir = new ArrayList<D>();
			file = new ArrayList<F>();
		}
		void add(String[] s, int d, int id){
			if(s.length-1==d){
				file.add(new F(id, s[d])); return;
			}
			for(D v:dir){
				if(v.name.equals(s[d])){
					v.add(s, d+1, id); return;
				}
			}
			D v = new D(s[d], this);
			dir.add(v);
			v.add(s, d+1, id);
		}
		int find(String[] s, int d){
//			System.out.println("S len:" + s.length + " depth:"+d+" cmd:"+s[d]);
			if(d==s.length-1){
				if("".equals(s[d])||".".equals(s[d])){
					for(F f:file){
						if("index.html".equals(f.name))return f.id;
					}
					return -1;
				}
				else if("..".equals(s[d])){
					if(parent==null)return -1;
					for(F f:parent.file){
						if("index.html".equals(f.name))return f.id;
					}
					return -1;
				}
				for(F f:file){
					if(s[d].equals(f.name))return f.id;
				}
				for(D v:dir){
					if(s[d].equals(v.name)){
						for(F f:v.file){
							if("index.html".equals(f.name))return f.id;
						}
					}
				}
				return -1;
			}
			if(".".equals(s[d]))return find(s, d+1);
			if("..".equals(s[d])){
				if(parent==null)return -1;
				return parent.find(s, d+1);
			}
			for(D v:dir){
				if(v.name.equals(s[d])){
					return v.find(s, d+1);
				}
			}
			return -1;
		}
		void dump(){
			System.out.println("Dir:" + name);
			System.out.println("FILES:");
			for(F f:file)System.out.println(f.name);
			System.out.println("DIRS:");
			for(D d:dir)System.out.println(d.name);
			for(D d:dir)d.dump();
		}
	}
	
	void run(){
//		System.out.println(("/ICPC/../ ").split("/").length);
		Scanner sc = new Scanner(System.in);
		for(;;){
			int n = sc.nextInt(), m = sc.nextInt();
			if((n|m)==0)break;
			D root = new D("", null);
			while(n--!=0){
				root.add(sc.next().split("/"), 1, n);
			}
//			root.dump();
			while(m--!=0){
				String s = sc.next();
				boolean f = false;
				if(s.charAt(s.length()-1)=='/'){
					s+=" "; f = true;
				}
				String[] t = s.split("/");
				if(f)t[t.length-1] = "";
				int a = root.find(t, 1);
//				System.out.println("A:" + a);
				s = sc.next();
				f = false;
				if(s.charAt(s.length()-1)=='/'){
					s+=" ";
					f = true;
				}
				t = s.split("/");
				if(f)t[t.length-1] = "";
				int b = root.find(t, 1);
//				System.out.println("B:"+b);
				System.out.println(a==-1||b==-1?"not found":a==b?"yes":"no");
			}
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}