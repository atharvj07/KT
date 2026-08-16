import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

//The Devil of Gravity
public class Main{

	class R implements Comparable<R>{
		int id, head, height;
		String s;
		public R(int id, int head, int height, String s) {
			this.id = id;
			this.head = head;
			this.height = height;
			this.s = s;
		}
		public int compareTo(R o) {
			return head-o.head;
		}
		public boolean inRange(){
			return head<=curpos&&curpos<=head+s.length();
		}
	}
	
	int id, curseg, curpos;
	Map<Integer, R> ref;
	LinkedList<List<R>> t;
	
	void fall(){
		boolean con = true;
		while(con){
			con = false;
			for(int i=1;i<t.size();i++)for(int j=0;j<t.get(i).size();j++){
				R r = t.get(i).get(j);
				boolean ok = true;
				for(R dw:t.get(i-1)){
					if(dw.head+dw.s.length()-1<r.head || r.head+r.s.length()-1<dw.head)continue;
					ok = false; break;
				}
				if(!ok)continue;
				t.get(i).remove(j);
				if(r.id==curseg)curseg = id;
				R v = new R(id, r.head, r.height-1, r.s);
				t.get(v.height).add(v);
				ref.put(id++, v);
				Collections.sort(t.get(v.height));
				j--;
				con = true;
			}
		}
	}
	
	void concat(){
		int h = ref.get(curseg).height;
		for(int i=0;i<t.size();i++)for(int j=0;j<t.get(i).size()-1;j++){
			R a = t.get(i).get(j);
			R b = t.get(i).get(j+1);
			if(a.head+a.s.length()==b.head){
				R v = new R(id, a.head, i, a.s+b.s);
				ref.put(id++, v);
				t.get(i).remove(j); t.get(i).remove(j);
				t.get(i).add(j, v);
				j--;
			}
		}
		for(R v:t.get(h)){
			if(v.inRange())curseg = v.id;
		}
	}
	
	void run(){
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		while(T--!=0){
			char[] s = sc.next().toCharArray();
			boolean error = false;
			id = 0;
			ref = new HashMap<Integer, R>();
			t = new LinkedList<List<R>>();
			for(int i=0;i<100;i++)t.add(new LinkedList<R>());
			R init = new R(id++, 0, 0, s[0]+"");
			ref.put(0, init);
			t.get(0).add(init);
			curseg = 0; curpos = 1;
			for(int i=1;i<s.length;i++){
				R r = ref.get(curseg);
//				System.out.println();
//				for(int h=2;h>=0;h--){
//					for(int j=0;j<t.get(h).size();j++)System.out.println(t.get(h).get(j).s);
//				}
				if(s[i]=='F'){
					if(r.head+r.s.length()==curpos){
						error = true; break;
					}
					curpos++;
				}
				else if(s[i]=='B'){
					if(r.head==curpos){
						error = true; break;
					}
					curpos--;
				}
				else if(s[i]=='P'){
					boolean hit = false;
					for(R up:t.get(r.height+1)){
						if(up.inRange()){
							hit = true;
							curseg = up.id;
							break;
						}
					}
					if(!hit){
						error = true; break;
					}
				}
				else if(s[i]=='N'){
					if(r.height==0){
						error = true; break;
					}
					boolean hit = false;
					for(R dw:t.get(r.height-1)){
						if(dw.inRange()){
							hit = true;
							curseg = dw.id;
							break;
						}
					}
					if(!hit){
						error = true; break;
					}
				}
				else if(s[i]=='D'){
					if(r.head+r.s.length()==curpos){
						error = true; break;
					}
					r.s = r.s.substring(0, curpos-r.head)+r.s.substring(curpos-r.head+1, r.s.length());
					if("".equals(r.s)){
						if(r.height==0){
							error = true; break;
						}
						boolean hit = false;
						for(R dw:t.get(r.height-1)){
							if(dw.inRange()){
								hit = true;
								for(int j=0;j<t.get(r.height).size();j++){
									if(t.get(r.height).get(j).id==curseg){
										t.get(r.height).remove(j); break;
									}
								}
								curseg = dw.id;
								break;
							}
						}
						if(!hit){
							error = true; break;
						}
					}
				}
				else if(s[i]=='C'){
					if(r.head+r.s.length()==curpos){
						error = true; break;
					}
					boolean hit = false;
					for(R up:t.get(r.height+1)){
						if(up.head<=curpos&&curpos<up.head+up.s.length()){
							hit = true; break;
						}
					}
					if(hit){
						error = true; break;
					}
					R v = new R(id, curpos, r.height+1, r.s.charAt(curpos-r.head)+"");
					ref.put(id, v);
					t.get(r.height+1).add(v);
					Collections.sort(t.get(r.height+1));
					curseg = id++;
					curpos++;
				}
				else{
					r.s = r.s.substring(0, curpos-r.head)+s[i]+r.s.substring(curpos-r.head, r.s.length());
					curpos++;
				}
				fall();
				concat();
			}
			System.out.println(error?"ERROR":ref.get(curseg).s);
		}
	}
	
	void debug(Object...o){
		System.out.println(Arrays.deepToString(o));
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}