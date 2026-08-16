import	java.util.*;
public	class	Main{
	public	static	void	main(String[]args){
		Scanner	cin=new	Scanner(System.in);
		int	x=cin.nextInt(),y=cin.nextInt(),s=Math.abs(x)+Math.abs(y);
		if(0>x){
			System.out.print(-s+" 0 0 ");
			if(0>y)	System.out.print(-s);
			else	System.out.print(s);
		}else{
			System.out.print("0 ");
			if(0>y)	System.out.print(-s);
			else	System.out.print(s);
			System.out.print(" "+s+" 0");
		}
	}
}
