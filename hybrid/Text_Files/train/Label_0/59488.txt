import java.util.*;
public class FSmartBoy {
	
	public static HashMap<String, Values> sub;
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		FSmartBoy instance = new FSmartBoy();
		int n = in.nextInt();
		
		int mLength = 0;
		String[] dict = new String[n];
		for (int i = 0; i < n; i++)
		{
			dict[i] = in.next();
			int l = dict[i].length();
			if (l > mLength)
				mLength = l;
		}
		
		sub = new HashMap<String, Values>();
		for (int word = 0; word < n; word++) { //Current word
			
			for (int i = 0; i < dict[word].length(); i++) //First index
			{
				
				for (int j = i + 1; j <= dict[word].length(); j++) //Index of end of substring
				{
					String str = dict[word].substring(i, j);
					//System.out.println(word + " : " + i + " : " + j + " : " + str);
					Object temp =  sub.get(str);
					
					if (temp == null) //If value not already in the map
					{
						Values nVal = instance.new Values(1);
						nVal.max = word;
						nVal.str = str;
						nVal.score = score(str, 1);
						sub.put(str, nVal);
					} else {  //If already in map
						Values nVal = (Values) temp;
						if (nVal.max == word) { //Break if already counted this word
							//System.out.print("BREAK");
							continue;
						}
						nVal.containing += 1;
						nVal.max = word;
						nVal.score = score(str, nVal.containing);
						sub.put(str, nVal);
					}
					
					}	
				}
			
		}
		
		//Tree has been built by now
		//-------------------------------------------
		
		//sub is the hashmap (contains every substring as keys and a Values object for the value of each key)
		//Values is the class of 
		
		Values ans=instance.new Values(n);
		ans.str="";
		dp(ans);
		if (ans.win==1) System.out.println("First"); else System.out.println("Second");
		System.out.println(ans.maxPoints+" "+ans.minPoints);
		
		/*
		System.out.println("\n\n\n---\n\n\n");
		for (Values val : sub.values())
		{
			System.out.println(val.str + ":" + val.containing + " : " + val.score);
			
		}
		*/
		
	}
	
	public static void dp(Values cu)
	{
		if (cu.minPoints==-1) {
		String s = cu.str;
		int loseMax=-1;
		int loseMin=Integer.MAX_VALUE;
		int winMax=-1;
		int winMin=Integer.MAX_VALUE;
		int w=0;
		for (int i=0;i<=25;i++)
		{
			String st = ((char) (i+97)) + s;
			Values ex = (Values) sub.get(st);
			if (ex!=null)
			{
				dp(ex);
				int tmax=ex.maxPoints;
				int tmin=ex.minPoints+ex.score;
				if (ex.win==1)
				{
					if (loseMax<tmin) {loseMax=tmin; loseMin=tmax;}
					else if ((loseMax==tmin) && (loseMin>tmax)) {loseMax=tmin; loseMin=tmax;};
				}
				else
				{
					w=1;
					if (winMax<tmin) {winMax=tmin; winMin=tmax;}
					else if ((winMax==tmin) && (winMin>tmax)) {winMax=tmin; winMin=tmax;};
				}
			}
			st = s+((char) (i+97));
			ex = (Values) sub.get(st);
			if (ex!=null)
			{
				dp(ex);
				int tmax=ex.maxPoints;
				int tmin=ex.minPoints+ex.score;
				if (ex.win==1)
				{
					if (loseMax<tmin) {loseMax=tmin; loseMin=tmax;}
					else if ((loseMax==tmin) && (loseMin>tmax)) {loseMax=tmin; loseMin=tmax;};
				}
				else
				{
					w=1;
					if (winMax<tmin) {winMax=tmin; winMin=tmax;}
					else if ((winMax==tmin) && (winMin>tmax)) {winMax=tmin; winMin=tmax;};
				}
			}
		}
		if ((loseMax==-1)&&(winMax==-1))
		{
			loseMax=0;
			loseMin=0;
			winMax=0;
			winMin=0;
		}
		if (w==1)
		{
			cu.maxPoints=winMax;
			cu.minPoints=winMin;
		}
		else
		{
			cu.maxPoints=loseMax;
			cu.minPoints=loseMin;
		}
		cu.win=w;
		//System.out.println(cu.str+" "+cu.win+" "+cu.maxPoints+" "+cu.minPoints);
		}
	}
	
	public static int score(String str, int num) //Calculates the score of a given string
	{
		int score = 0;
		char[] cArr = str.toCharArray();
		for (int i = 0; i < cArr.length; i++)
		{
			cArr[i] = (char) (cArr[i] - 'a' + 1);
		}
		
		int max = 0;
		for (int i = 0; i < cArr.length; i++) {
			score += cArr[i];
			if (cArr[i] > max)
				max = cArr[i];
		}
		score *= max;
		score += num;
		return score;
		
			
			
		}
		
	
	
	public class Values
	{
		public int containing; //Number of words containing
		public int score;      //Score of the substring
		public int maxPoints=-1;
		public int minPoints=-1;
		public int max = -1;
		public String str; //String value
		public int win=2;
		
		public Values(int containing)
		{
			this.containing = containing;
		}
		
		
	}

	

}

