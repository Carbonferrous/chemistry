class Lement
{
	private String name;
	private double mass;
	private int protons;
	private int neutrons;
	private int[][][][] electrons;
	private double electronegativity;
	//Constructors
	public Lement(int p)
	{
		//readData from "Lement_Data"
	}
	public void fillElectrons(int count)
	{
		int n = 1;
		int l = 0;
		for(int s = 1; s < 9; s ++)
		{
			if(count <= 0)
				break;
			n = s/2 + 1;
			l = s - n;
			while(l > -1 && l < n)
			{
				for(int m = -l; m < l + 1; m ++)
				{
					electrons[n-1][l][m+l][0] = 1;
					count --;
					if(count <= 0)
						break;
				}
				if(count <= 0)
					return;
				for(int m = -l; m < l + 1; m ++)
				{
					electrons[n-1][l][m+l][1] = -1;
					count --;
					if(count <= 0)
						break;
				}
				n ++;
				l --;
				if(count <= 0)
					break;
			}
			if(count <= 0)
				break;
		}
	}
	public void exciteElectron(nstart, lstart, nend, lend)
	{
		
	}
//	excite electrons
//	add bonding electrons
	//Accessors
//	public String name()
//	public double getMass()
//	public int getProtons()
//	public int getNeutrons()
//	public Tree<Integer> getElectrons()
//	public double getElectronegativity()
	//Setters
//	public void setName(String n)
//	public void setMass(double m) //Must check that within reasonable bounds of Neutrons + Protons
//	public void setNeutrons(int n)
//	public void setElectrons(boolean[] e)//or maybe swap electrons, check charge is not too large
	//Bonds/e
	//bond type(Ionic, Covalent), sigma, pi, Strength
	//create bonds, fill electrons, electron configuration, bond type, magnetism
//	public boolean getMagnetism() //False - Paramagnetic, True - Diamagnetic
//	public String getElectronConfiguration()
//	public int getCharge()
}