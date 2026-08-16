import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

//Dimensional Analysis
public class Main{

	char[] s;
	int id;
	char get(){
		return s[id++];
	}
	
	int[][] q;
	Map<String, Integer> ref;
	String[] name;
	int ID;
	void reg(String s){
		if(ref.containsKey(s))return;
		name[ID] = s;
		ref.put(s, ID++);
	}
	int n, m, p;
	boolean error;
	Map<String, String> var;
	
	int[] formula(){
		int[] res = term();
		for(;;){
			char ch = get();
			if(ch=='+'||ch=='-'){
				int[] t = term();
				for(int i=0;i<n;i++)if(res[i]!=t[i])error = true;
			}
			else break;
		}
		id--;
		return res;
	}
	
	int[] term(){
		int[] res = factor();
		for(;;){
			char ch = get();
			if(ch=='*'){
				int[] f = factor();
				for(int i=0;i<n;i++)res[i]+=f[i];
			}
			else if(ch=='/'){
				int[] f = factor();
				for(int i=0;i<n;i++)res[i]-=f[i];
			}
			else break;
		}
		id--;
		return res;
	}
	
	int[] factor(){
		char ch = get();
		if(ch=='('){
			int[] res = formula();
			get();
			return res;
		}
		String t = "";
		while(Character.isUpperCase(ch)||Character.isLowerCase(ch)){
			t+=ch; ch = get();
		}
		id--;
		int[] res = new int[n];
		int idx = ref.get(var.get(t));
		for(int i=0;i<n;i++)res[i]=q[idx][i];
		return res;
	}
	
	void run(){
		Scanner sc = new Scanner(System.in);
		for(;;){
			n = sc.nextInt(); m = sc.nextInt(); p = sc.nextInt();
			if((n|m|p)==0)break;
			ref = new HashMap<String, Integer>();
			ID = 0;
			name = new String[m];
			q = new int[m][n];
			for(int i=0;i<m;i++){
				reg(sc.next());
				for(int j=0;j<n;j++)q[i][j]=sc.nextInt();
			}
			s = (sc.next()+"$").toCharArray();
			id = 0;
			var = new HashMap<String, String>();
			while(p--!=0)var.put(sc.next(), sc.next());
			error = false;
			int[] res = formula();
			if(error){
				System.out.println("error"); continue;
			}
			String r = "undefined";
			for(int i=0;i<m;i++){
				boolean ok = true;
				for(int j=0;j<n;j++)if(res[j]!=q[i][j])ok = false;
				if(ok)r = name[i];
			}
			System.out.println(r);
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}