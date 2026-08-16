import java.io.*;
import java.util.*;

public class Main{
	public static void main(String args[]){
		try{
			new Main();
		}catch(IOException err){
			err.printStackTrace();
		}
	}
	
	public Main() throws IOException{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		List<Integer> Ans = new ArrayList<Integer>();
		String line;
		
		while((line = in.readLine()) != null){
			int isGood = 0;
			int size = Integer.parseInt(line);
			
			if(size==0) break;
			
			List<Integer> ids = new ArrayList<Integer>();
			List<Long> sales = new ArrayList<Long>();
			
			for(int n=0; n<size; n++){
				line = in.readLine();
				String[] dst = line.split(" ");
				int id = Integer.parseInt(dst[0]);
				int price = Integer.parseInt(dst[1]);
				int num = Integer.parseInt(dst[2]);
				long sale = (long)price * (long)num;
				
				if(!ids.contains(id)){
					ids.add(id);
					sales.add(sale);
				}
				else{
					int index = ids.indexOf(id);
					sale = sale + sales.get(index);
					sales.set(index, sale);
				}
			}
			
			for(int n=0; n<ids.size(); n++){
				if(sales.get(n) >= 1000000){
					Ans.add(ids.get(n));
					isGood = 1;
				}
			}
			
			if(isGood == 0){
				Ans.add(-1);
			}
		}
		
		for(int n=0; n<Ans.size(); n++){
			if(Ans.get(n)==-1){
				System.out.println("NA");	
			}
			else{
				System.out.println(Ans.get(n));
			}
		}
	}
}