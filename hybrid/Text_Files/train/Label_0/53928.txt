import java.util.Scanner;
public class IcePEace {

	public static int searchstring(String s,String S){
		if (s.length()>S.length())
			return -1;
		for(int i=0;i<=(S.length()-s.length());i++){
			if (s.equals(S.substring(i,i+s.length())))
				return i;
		}
		return -1;
	}
	public static String removestring(String s, int i){
		if (i == (s.length()-1)){
			s=s.substring(0, i);
			return s;
		}
		if (i==0){
			s=s.substring(1,s.length());
			return s;
		}
		if (i>=s.length()){
			return s;
		}
		s=s.substring(0,i)+s.substring(i+1, s.length());
		return s;
	}

	public static void main(String[] args){
		
		
		Scanner sc = new Scanner(System.in);
		String t = sc.nextLine();
		String ice = sc.nextLine();
		int Boole = 0;			
		int possibilities = 0;
		int i = 0;
		int j = 0;
		String na = "";
		while (ice.length()>0){
			//System.out.println("start of outer loop");
			if (ice.length()<t.length())
				break;			
			j=0;
			while ((Boole>-1)&&(j<t.length())&&(ice.length()>0)){
				//System.out.println("Start of inner loop");
				na = t.substring(j,j+1);
				
				if ((na.equals("2")) || (na.equals("5"))){
					Boole = searchstring("2",ice);
					//System.out.println("searching for 2");
					if (Boole == -1){
						//System.out.println("searching for 5");
						Boole = searchstring("5",ice);
					}
					if (Boole != -1){
						ice=removestring(ice,Boole);
					}
				}
				else if (na.equals("6")||na.equals("9")){
						Boole = searchstring("6",ice);
						if (Boole == -1){
							Boole = searchstring("9",ice);
						}
						if (Boole != -1){
							ice=removestring(ice,Boole);
						}
					}
					else {
						//System.out.println("search the char");
						Boole = searchstring(na,ice);
						if (Boole != -1){		
							//System.out.println(ice + " before edit");
							ice=removestring(ice,Boole);
							//System.out.println( ice+ " after edit");
					}
					}
				++j;
				
		}
			
			if (Boole != -1){
				++possibilities;
			}
			else
				break;
			//System.out.println("end of outer loop , ice = " + ice);
			
		
	}
		System.out.println(possibilities);
}
}