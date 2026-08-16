import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

//Unit Converter
public class Main{

	void run(){
		Map<String, Integer> ref = new HashMap<String, Integer>();
		ref.put("yotta", 24); ref.put("zetta", 21); ref.put("exa", 18); ref.put("peta", 15); ref.put("tera", 12);
		ref.put("giga", 9); ref.put("mega", 6); ref.put("kilo", 3); ref.put("hecto", 2); ref.put("deca", 1);
		ref.put("deci", -1); ref.put("centi", -2); ref.put("milli", -3); ref.put("micro", -6); ref.put("nano", -9);
		ref.put("pico", -12); ref.put("femto", -15); ref.put("ato", -18); ref.put("zepto", -21); ref.put("yocto", -24);
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt(); sc.nextLine();
		while(T--!=0){
			String[] t = sc.nextLine().split(" ");
			char[] s = null;
			int p = 0, K = 0;
			String w = "";
			if(t[0].contains(".")){
				p = t[0].indexOf('.')-1;
				t[0] = t[0].substring(0, p+1)+t[0].substring(p+2);
//				t[0].replaceAll("\\.", "");
//				System.out.println("T:"+t[0]);
				s = t[0].toCharArray();
			}
			else{
				p = t[0].length()-1;
				s = t[0].toCharArray();
			}
			if(t.length==2){
				w = t[1];
			}
			else{
				w = t[2]; p+=ref.get(t[1]);
			}
			int k = 0;
			while(s[k]=='0')k++;
			K = s.length-k;
			int exp = k<p?p-k:p-k;
			StringBuilder res = new StringBuilder();
			res.append(s[k]+"");
			if(K>1){
				res.append(".");
				for(int i=k+1;i<s.length;i++)res.append(s[i]);
			}
			System.out.println(res.toString()+" * 10^"+exp+" "+w);
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}