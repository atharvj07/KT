import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

//Reading a Chord
public class Main{

	boolean ok(boolean[] a, boolean[] b){
		for(int i=0;i<12;i++)if(a[i]!=b[i])return false;
		return true;
	}
	
	void run(){
		Scanner sc = new Scanner(System.in);
		String[] tones = {"C","C#","D","D#","E","F","F#","G","G#","A","A#","B"};
		String[] add = {"","7","M7","m","m7"};
		int[][] adds = {{4,7},{4,7,10},{4,7,11},{3,7},{3,7,10}};
		String[] tension = {"","-9","9","+9","-11","11","+11","","-13","13","+13"};
		int T = sc.nextInt();
		while(T--!=0){
			int n = sc.nextInt();
			boolean[] t = new boolean[12];
			for(int i=0;i<n;i++){
				String c = sc.next();
				for(int k=0;k<12;k++)if(tones[k].equals(c)){
					t[k] = true; break;
				}
			}
			List<String> res = new ArrayList<String>();
			for(int b=0;b<12;b++)for(int a=0;a<5;a++){
				boolean[] r = new boolean[12];
				r[b] = true;
				for(int k:adds[a])r[(b+k)%12] = true;
				if(ok(r, t)){
					res.add(tones[b]+add[a]); continue;
				}
				for(int k=1;k<11;k++){
					if(k==7)continue;
					int x = (b+k)%12;
					boolean p = r[x];
					r[x] = true;
					if(ok(r, t))res.add(tones[b]+add[a]+"("+tension[k]+")");
					r[x] = p;
				}
				r[(b+7)%12] = false; r[(b+18)%12] = true;
				if(ok(r, t))res.add(tones[b]+add[a]+"(-5)");
				r[(b+18)%12] = false; r[(b+8)%12] = true;
				if(ok(r, t))res.add(tones[b]+add[a]+"(+5)");
			}
			if(res.isEmpty())System.out.println("UNKNOWN");
			else{
				for(int i=0;i<res.size();i++)System.out.print(res.get(i)+(i==res.size()-1?"\n":" "));
			}
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}