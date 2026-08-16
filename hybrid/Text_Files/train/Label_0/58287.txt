import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;
import static java.lang.Math.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;

public class Main{

	Scanner sc=new Scanner(System.in);

	int plen, cnum, width, cspace;
	ArrayList<String> lines;

	void run(){
		for(;;){
			plen=sc.nextInt();
			if(plen==0){
				break;
			}
			cnum=sc.nextInt();
			width=sc.nextInt();
			cspace=sc.nextInt();
			sc.nextLine();
			lines=new ArrayList<String>();
			for(;;){
				String line=sc.nextLine();
				if(line.equals("?")){
					break;
				}
				lines.add(line);
			}
			solve();
		}
	}

	void solve(){
		ArrayList<String> list=new ArrayList<String>();
		for(String s : lines){
			for(;;){
				if(s.length()<=width){
					for(; s.length()<width;){
						s+=".";
					}
					list.add(s);
					break;
				}else{
					list.add(s.substring(0, width));
					s=s.substring(width, s.length());
				}
			}
		}
		// debug(list);
		String dot="";
		for(; dot.length()<width;){
			dot+=".";
		}
		for(; list.size()%(plen*cnum)!=0;){
			list.add(dot);
		}
		String space="";
		for(; space.length()<cspace;){
			space+=".";
		}
		// debug(list);
		// debug(list.size());
		for(int k=0; k<list.size()/(plen*cnum); k++){
			for(int i=0; i<plen; i++){
				for(int j=0; j<cnum; j++){
					String s=list.get(i+j*plen+k*plen*cnum);
					print(s);
					if(j<cnum-1){
						print(space);
					}
				}
				println("");
			}
			println("#");
		}
		println("?");
	}

	void debug(Object... os){
		System.err.println(deepToString(os));
	}

	void print(String s){
		System.out.print(s);
	}

	void println(String s){
		System.out.println(s);
	}

	public static void main(String[] args){
		new Main().run();
	}

}