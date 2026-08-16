import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str,strArray[];
		int a=0,b=0,ab=0,o=0;

		while((str=br.readLine()) != null){
			strArray = str.split(",");

			if(strArray[1].equals("A")){
				a++;
			}else if(strArray[1].equals("B")){
				b++;
			}else if(strArray[1].equals("AB")){
				ab++;
			}else{
				o++;
			}
		}

		System.out.printf("%d\n%d\n%d\n%d\n",a,b,ab,o);

	}
}