"""
AI Agents for YourCarbonFootprint Bangladesh application.
Uses CrewAI to create agents for various tasks specific to Bangladesh context.
"""

import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM

# Load environment variables
load_dotenv()

# Get Groq API key
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Initialize LLM
def get_llm():
    """Initialize and return the Groq LLM."""
    return LLM(
        model="groq/llama-3.3-70b-versatile",
        temperature=0.7
    )

# Create AI agents specialized for Bangladesh
class BangladeshCarbonFootprintAgents:
    def __init__(self):
        """Initialize the BangladeshCarbonFootprintAgents class."""
        self.llm = get_llm()
        self._create_agents()
    
    def _create_agents(self):
        """Create all the agents with Bangladesh-specific context."""
        
        # Data Entry Assistant for Bangladesh
        self.data_entry_assistant = Agent(
            llm=self.llm,
            role="Bangladesh Carbon Data Entry Assistant",
            goal="Help Bangladesh-based companies classify emissions, map to scopes, and validate data entries with local context",
            backstory="You are an expert in carbon accounting with deep knowledge of Bangladesh's "
                     "industrial landscape, including RMG, textiles, jute, leather, pharmaceuticals, "
                     "and other key sectors. You understand the unique challenges of Bangladesh "
                     "businesses like frequent power outages requiring diesel generators, seasonal "
                     "flooding impacts, and the specific emission factors for Bangladesh's electricity "
                     "grid (0.6815 kgCO2e/kWh). You help companies correctly categorize their "
                     "emissions considering local conditions and practices.",
            allow_delegation=False,
            verbose=False
        )
        
        # Report Summary Generator for Bangladesh
        self.report_generator = Agent(
            llm=self.llm,
            role="Bangladesh Carbon Report Generator",
            goal="Convert emission data into comprehensive summaries tailored for Bangladesh businesses and export requirements",
            backstory="You are a skilled analyst specializing in Bangladesh's industrial sectors. "
                     "You understand the importance of carbon reporting for Bangladesh's major "
                     "export industries (RMG, textiles, leather, jute) and their compliance "
                     "requirements for international markets, especially EU CBAM regulations. "
                     "You can identify trends specific to Bangladesh's industrial patterns, "
                     "monsoon impacts, and energy challenges. You make complex carbon data "
                     "accessible to SME owners and export-oriented businesses.",
            allow_delegation=False,
            verbose=False
        )
        
        # Carbon Offset Advisor for Bangladesh
        self.offset_advisor = Agent(
            llm=self.llm,
            role="Bangladesh Carbon Offset Advisor",
            goal="Suggest verified offset options and local carbon reduction projects suitable for Bangladesh context",
            backstory="You are a sustainability expert with extensive knowledge of Bangladesh's "
                     "environmental landscape and carbon offset opportunities. You understand "
                     "local reforestation projects (like Sundarbans conservation), solar and "
                     "biogas initiatives, and Bangladesh's renewable energy potential. You know "
                     "about local organizations, government initiatives like the Mujib Climate "
                     "Prosperity Plan, and can recommend both international verified carbon "
                     "credits and local sustainability projects that align with Bangladesh's "
                     "development goals and cultural values.",
            allow_delegation=False,
            verbose=False
        )
        
        # Regulation Radar for Bangladesh
        self.regulation_radar = Agent(
            llm=self.llm,
            role="Bangladesh Export Regulation Specialist",
            goal="Track and explain carbon-related regulations affecting Bangladesh exporters and businesses",
            backstory="You are a regulatory expert focused on Bangladesh's position in global "
                     "carbon regulations. You track EU CBAM requirements affecting Bangladesh's "
                     "steel, cement, aluminum, and fertilizer exports, US sustainability "
                     "requirements for textile imports, and emerging regulations in other key "
                     "export markets. You understand Bangladesh's NDC commitments, the Delta "
                     "Plan 2100, and local environmental regulations. You help export-oriented "
                     "SMEs navigate complex international carbon compliance requirements while "
                     "considering Bangladesh's developing country status and available support mechanisms.",
            allow_delegation=False,
            verbose=False
        )
        
        # Emission Optimizer for Bangladesh
        self.emission_optimizer = Agent(
            llm=self.llm,
            role="Bangladesh Industrial Emission Optimizer",
            goal="Provide practical emission reduction strategies tailored to Bangladesh's industrial context and constraints",
            backstory="You are a carbon reduction specialist with deep understanding of "
                     "Bangladesh's industrial challenges and opportunities. You know the "
                     "constraints of frequent power outages, infrastructure limitations, "
                     "and capital constraints faced by SMEs. You can suggest practical "
                     "solutions like solar installations, energy-efficient equipment available "
                     "in Bangladesh, waste heat recovery for textile mills, biogas from "
                     "agricultural waste, and efficiency improvements in RMG factories. "
                     "You understand local supply chains, available technologies, financing "
                     "options through banks like IDCOL, and government incentives for "
                     "green initiatives.",
            allow_delegation=False,
            verbose=False
        )
    
    def create_data_entry_task(self, data_description):
        """Create a task for the Bangladesh Data Entry Assistant."""
        return Task(
            description=(
                f"Analyze the following emission activity from a Bangladesh business context: {data_description}\n"
                f"Consider the following Bangladesh-specific factors:\n"
                f"1. Determine if this is Scope 1, 2, or 3 emissions\n"
                f"2. Suggest the most appropriate category considering Bangladesh industries\n"
                f"3. Recommend appropriate emission factors using Bangladesh grid factor (0.6815 kgCO2e/kWh for electricity)\n"
                f"4. Consider common Bangladesh practices like diesel generator backup during load shedding\n"
                f"5. Validate data quality and suggest improvements for export compliance\n"
                f"6. Mention any specific considerations for RMG, textiles, jute, leather, or other key Bangladesh sectors"
            ),
            expected_output="A detailed classification with Bangladesh-specific context, appropriate "
                           "emission factors, and sector-specific guidance for accurate carbon accounting.",
            agent=self.data_entry_assistant
        )
    
    def create_report_summary_task(self, emissions_data):
        """Create a task for the Bangladesh Report Summary Generator."""
        return Task(
            description=(
                f"Generate a comprehensive summary of emissions data for a Bangladesh business: {emissions_data}\n"
                f"Focus on:\n"
                f"1. Key emission patterns relevant to Bangladesh industrial context\n"
                f"2. Comparison with typical Bangladesh industry benchmarks\n"
                f"3. Impact of power outages and diesel backup generators\n"
                f"4. Readiness for export market requirements (EU CBAM, US sustainability standards)\n"
                f"5. Seasonal variations and monsoon impacts if applicable\n"
                f"6. Opportunities for improvement using locally available solutions\n"
                f"7. Compliance status for major export markets"
            ),
            expected_output="A comprehensive report summary with Bangladesh-specific insights, "
                           "export readiness assessment, and actionable recommendations.",
            agent=self.report_generator
        )
    
    def create_offset_advice_task(self, emissions_total, location, industry):
        """Create a task for the Bangladesh Carbon Offset Advisor."""
        return Task(
            description=(
                f"Recommend carbon offset and reduction strategies for a Bangladesh business:\n"
                f"- Total emissions: {emissions_total} kgCO2e\n"
                f"- Location: {location}\n"
                f"- Industry: {industry}\n"
                f"Focus on:\n"
                f"1. Local carbon offset projects in Bangladesh (reforestation, biogas, solar)\n"
                f"2. International verified carbon credits suitable for export compliance\n"
                f"3. Government programs and incentives available in Bangladesh\n"
                f"4. IDCOL and other financing options for green projects\n"
                f"5. Community-based offset projects that support local development\n"
                f"6. Cost estimates in BDT and USD\n"
                f"7. Alignment with Bangladesh's NDC and Mujib Climate Prosperity Plan"
            ),
            expected_output="A tailored list of offset options with local and international choices, "
                           "costs in local currency, financing options, and implementation guidance.",
            agent=self.offset_advisor
        )
    
    def create_regulation_check_task(self, location, industry, export_markets):
        """Create a task for the Bangladesh Regulation Radar."""
        return Task(
            description=(
                f"Analyze regulatory requirements for a Bangladesh exporter:\n"
                f"- Location: {location}\n"
                f"- Industry: {industry}\n"
                f"- Export markets: {export_markets}\n"
                f"Provide analysis on:\n"
                f"1. EU CBAM requirements and timeline (especially for steel, cement, textiles)\n"
                f"2. US sustainability requirements for textile and apparel imports\n"
                f"3. Other destination market carbon requirements\n"
                f"4. Bangladesh's NDC commitments and local regulations\n"
                f"5. Support available through government agencies (BSTI, BGMEA, BKMEA)\n"
                f"6. Compliance roadmap with specific timelines\n"
                f"7. Documentation requirements for export markets\n"
                f"8. Potential impacts of non-compliance on export business"
            ),
            expected_output="A comprehensive regulatory analysis with compliance roadmap, "
                           "support resources, and specific action items for Bangladesh exporters.",
            agent=self.regulation_radar
        )
    
    def create_optimization_task(self, emissions_data):
        """Create a task for the Bangladesh Emission Optimizer."""
        return Task(
            description=(
                f"Analyze emissions data and provide Bangladesh-specific reduction strategies: {emissions_data}\n"
                f"Consider:\n"
                f"1. Top emission sources that can be addressed with locally available solutions\n"
                f"2. Solar power potential given Bangladesh's solar irradiation\n"
                f"3. Energy efficiency measures for textile mills, RMG factories, etc.\n"
                f"4. Waste heat recovery and cogeneration opportunities\n"
                f"5. Biogas from agricultural and industrial waste\n"
                f"6. Replacement of diesel generators with cleaner alternatives\n"
                f"7. Water and waste management improvements\n"
                f"8. Supply chain optimization for reduced transport emissions\n"
                f"9. Cost-benefit analysis in BDT\n"
                f"10. Available financing through IDCOL, commercial banks, or development partners\n"
                f"11. Implementation timeline considering monsoon and production cycles"
            ),
            expected_output="A prioritized action plan with practical, cost-effective solutions "
                           "tailored to Bangladesh's industrial context, including costs, timelines, and financing options.",
            agent=self.emission_optimizer
        )
    
    def run_data_entry_crew(self, data_description):
        """Run a crew with the Bangladesh Data Entry Assistant."""
        task = self.create_data_entry_task(data_description)
        crew = Crew(
            agents=[self.data_entry_assistant],
            tasks=[task],
            verbose=False
        )
        return crew.kickoff()
    
    def run_report_summary_crew(self, emissions_data):
        """Run a crew with the Bangladesh Report Summary Generator."""
        task = self.create_report_summary_task(emissions_data)
        crew = Crew(
            agents=[self.report_generator],
            tasks=[task],
            verbose=False
        )
        return crew.kickoff()
    
    def run_offset_advice_crew(self, emissions_total, location, industry):
        """Run a crew with the Bangladesh Carbon Offset Advisor."""
        task = self.create_offset_advice_task(emissions_total, location, industry)
        crew = Crew(
            agents=[self.offset_advisor],
            tasks=[task],
            verbose=False
        )
        return crew.kickoff()
    
    def run_regulation_check_crew(self, location, industry, export_markets):
        """Run a crew with the Bangladesh Regulation Radar."""
        task = self.create_regulation_check_task(location, industry, export_markets)
        crew = Crew(
            agents=[self.regulation_radar],
            tasks=[task],
            verbose=False
        )
        return crew.kickoff()
    
    def run_optimization_crew(self, emissions_data):
        """Run a crew with the Bangladesh Emission Optimizer."""
        task = self.create_optimization_task(emissions_data)
        crew = Crew(
            agents=[self.emission_optimizer],
            tasks=[task],
            verbose=False
        )
        return crew.kickoff()

# Backward compatibility - create an alias
CarbonFootprintAgents = BangladeshCarbonFootprintAgents