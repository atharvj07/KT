
import java.io.*;
public class Main {
	public static void main(String[] args) throws IOException{
BufferedReader buffer = new BufferedReader(new InputStreamReader(System.in));
int m = Integer.parseInt(buffer.readLine());
String[]line = new String[m];
for(int i=0;i<m;i++)
line[i] = buffer.readLine();
word(m,line);
}
	public static void word(int m,String[]line){
		String miao="miao.";
		String lola="lala.";
		for(int i=0;i<m;i++){
			if(line[i].length()<5){
				System.out.println("OMG>.< I don't know!");}
			else{String first = line[i].substring(0,5);
			String last = line[i].substring(line[i].length()-5,line[i].length());
			if(lola.compareTo(last)==miao.compareTo(first))
				System.out.println("OMG>.< I don't know!");
			else if(miao.compareTo(first)==0)
				System.out.println("Rainbow's");
			else if(lola.compareTo(last)==0)
				System.out.println("Freda's");
			else
				System.out.println("OMG>.< I don't know!");
		}}
	}
}