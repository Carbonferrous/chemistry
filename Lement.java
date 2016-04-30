class Lement
{
	private String name;
	private double mass;
	private int protons;
	private int neutrons;
//	private boolean[] electrons;
	private double electronegativity;
//	private ArrayList<Bonds> bonds;
	//Constructors
	public Lement(int p)
	{
		//readData from "Lement_Data"
	}
	//Accessors
	public String name()
	public double getMass()
	public int getProtons()
	public int getNeutrons()
//	public boolean[] getElectrons()
	public double getElectronegativity()
	//Setters
	public void setName(String n)
	public void setMass(double m) //Must check that within reasonable bounds of Neutrons + Protons
	public void setNeutrons(int n)
//	public void setElectrons(boolean[] e)//or maybe swap electrons, check charge is not too large
	//Bonds/e
	//bond type(Ionic, Covalent), sigma, pi, Strength
	//create bonds, fill electrons, electron configuration, bond type, magnetism
//	public boolean getMagnetism() //False - Paramagnetic, True - Diamagnetic
//	public String getElectronConfiguration()
	public int getCharge()
}