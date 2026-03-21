import json
import re

def get_service_content(title):
    t_lower = title.lower()
    
    # Defaults
    content = {
        "image": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&q=80&w=2000",
        "requirements": [
            "Passport copy of shareholders and directors",
            "Visa copy or entry stamp (if applicable)",
            "NOC from current sponsor (if required)",
            "Proof of address (utility bill or tenancy contract)",
            "Business profile or brief description of activities"
        ],
        "steps": [
            {"title": "Initial Consultation", "desc": "We guide you on requirements, best structures, and upcoming procedures."},
            {"title": "Document Collection", "desc": "Submit required documents for our legal review team."},
            {"title": "Application Submission", "desc": "We submit your application and fees to the relevant regulatory authority."},
            {"title": "Approval & Handover", "desc": "Collect your final documents and receive immediate operational guidance."}
        ]
    }
    
    # Category: Visa & Immigration
    if "visa" in t_lower or "entry permit" in t_lower or "emirates id" in t_lower or "status change" in t_lower:
        content["image"] = "https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?auto=format&fit=crop&q=80&w=2000"
        content["requirements"] = [
            "Clear color copy of passport (minimum 6 months validity)",
            "Passport-size photographs with white background",
            "Sponsor's Emirates ID and Visa copy (for dependents)",
            "Trade License copy (for investors/partners)",
            "Attested degree/certificates (if applicable for profession)"
        ]
        content["steps"] = [
            {"title": "Application & Entry Permit", "desc": "We apply for the initial Entry Permit (E-Visa) allowing legal entry or status change."},
            {"title": "Status Change", "desc": "If inside the UAE, we process your status change without needing to exit the country."},
            {"title": "Medical Fitness Test", "desc": "We schedule and guide you through the mandatory VIP or standard medical testing."},
            {"title": "Emirates ID & Visa Stamping", "desc": "Biometrics registration followed by the final residence visa issuance."}
        ]
        if "family" in t_lower:
            content["image"] = "https://images.unsplash.com/photo-1511895426328-dc8714191300?q=80&w=2000"
            content["requirements"].append("Attested Marriage/Birth certificates")
            
    # Category: Licensing & Registration
    elif "license" in t_lower:
        if "e-commerce" in t_lower:
            content["image"] = "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?q=80&w=2000"
            content["requirements"].append("Details of the website or digital platform")
        elif "industrial" in t_lower:
            content["image"] = "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=2000"
            content["requirements"].append("Warehouse/Factory lease agreement")
            content["requirements"].append("Environmental clearance approvals")
        elif "commercial" in t_lower or "trade" in t_lower:
            content["image"] = "https://images.unsplash.com/photo-1444653614773-995cb1ef9efa?q=80&w=2000"
            
        content["steps"] = [
            {"title": "Trade Name Registration", "desc": "We reserve your preferred business name with the economic department."},
            {"title": "Initial Approval", "desc": "Securing preliminary consent from the government for your specific business activities."},
            {"title": "Ejari / Lease Agreement", "desc": "Finalizing your office or facility space and registering the tenancy contract."},
            {"title": "License Issuance", "desc": "Submitting all final documents to instantly issue the Trade License."}
        ]

    # Category: Company Formation
    elif "incorporation" in t_lower or "formation" in t_lower or "setup" in t_lower:
        content["image"] = "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=2000"
        content["requirements"] = [
            "Passport copy of shareholders and directors",
            "Proposed business names (3 options)",
            "Outline of planned business activities",
            "NOC from current sponsor (if UAE resident)",
            "Proof of residence (utility bill)"
        ]
        if "offshore" in t_lower:
            content["image"] = "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=2000"
            content["requirements"].append("Bank reference letter")
            content["requirements"].append("CV/Resume of shareholders")
            
        content["steps"] = [
            {"title": "Jurisdiction Advisory", "desc": "Selecting the perfect Free Zone, Mainland, or Offshore authority for your goals."},
            {"title": "Application Filing", "desc": "Preparing the Memorandum of Association (MOA) and submitting shareholder details."},
            {"title": "Corporate Bank Account", "desc": "Connecting you with premium banking partners for seamless account opening."},
            {"title": "Final Company Documents", "desc": "Receiving your License, Certificate of Incorporation, and Share Certificates."}
        ]

    # Category: Corporate Admin (Tax, VAT, Audit, Liquidate)
    elif "vat" in t_lower or "tax" in t_lower or "audit" in t_lower or "payroll" in t_lower or "liquidation" in t_lower or "advisory" in t_lower:
        content["image"] = "https://images.unsplash.com/photo-1554224155-6726b3ff858f?q=80&w=2000"
        if "audit" in t_lower:
            content["image"] = "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?q=80&w=2000"
            
        content["requirements"] = [
            "Copy of Trade License and MOA",
            "Emirates ID of the authorized signatory",
            "Company Bank Statements (last 6-12 months)",
            "Existing financial records or ledgers",
            "Tenancy contract (Ejari)"
        ]
        content["steps"] = [
            {"title": "Financial Assessment", "desc": "Our accountants review your current financial standing and corporate records."},
            {"title": "Documentation Preparation", "desc": "We organize, audit, and compile your books according to UAE IFRS standards."},
            {"title": "Portal Submission", "desc": "Filing your returns, reports, or registration via the Federal Tax Authority (FTA) portal."},
            {"title": "Compliance Confirmation", "desc": "Delivering your Tax Registration Number (TRN) or final audit clearance reports."}
        ]

    # Category: Brands & Web
    elif "brand" in t_lower or "website" in t_lower or "marketing" in t_lower or "growth" in t_lower:
        content["image"] = "https://images.unsplash.com/photo-1542744173-8e7e53415bb0?q=80&w=2000"
        if "website" in t_lower:
            content["image"] = "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?q=80&w=2000"
        elif "marketing" in t_lower:
            content["image"] = "https://images.unsplash.com/photo-1533750516457-a7f992034fec?q=80&w=2000"
            
        content["requirements"] = [
            "High-resolution company logo",
            "Valid UAE Trade License",
            "Power of Attorney (for trademark filing)",
            "Brand guidelines or specific color schemes",
            "List of products/services to protect or market"
        ]
        content["steps"] = [
            {"title": "Strategy Workshop", "desc": "Understanding your target audience, digital goals, and brand aesthetic."},
            {"title": "Design & Execution", "desc": "Creating wireframes, marketing campaigns, or trademark application drafts."},
            {"title": "Review & Registration", "desc": "Filing with the Ministry of Economy or launching the digital platform."},
            {"title": "Monitoring & Handover", "desc": "Receiving your Trademark Certificate or final website credentials."}
        ]

    # Category: PRO & Government (Attestation, MOA, Typing)
    elif "government" in t_lower or "attestation" in t_lower or "moa" in t_lower or "notary" in t_lower or "typing" in t_lower or "ejari" in t_lower:
        content["image"] = "https://images.unsplash.com/photo-1589829085413-56de8ae18c73?q=80&w=2000"
        content["requirements"] = [
            "Original documents to be processed/attested",
            "Passport and Visa copies of involved parties",
            "Company Trade License",
            "Authorization letter / Power of Attorney"
        ]
        content["steps"] = [
            {"title": "Document Collection", "desc": "Secure pickup of your original documents from your location."},
            {"title": "Translation & Typing", "desc": "Legally translating and formatting documents for government acceptance."},
            {"title": "Authority Submission", "desc": "Processing through Notary Public, MOFA, or respective Embassies."},
            {"title": "Secure Delivery", "desc": "Safe return of your attested, legally stamped documents directly to you."}
        ]
        
    return content

def make_service(title, filename, parent_link="services.html", parent_name="Services", color="indigo"):
    content = get_service_content(title)
    return {
        "title": title,
        "filename": filename,
        "parent_link": parent_link,
        "parent_name": parent_name,
        "color": color,
        "image": content["image"],
        "hero_desc": f"Professional and seamless execution of your {title} in the UAE. We eliminate the red tape so you can focus on growth.",
        "about_title": f"Why choose our {title} service?",
        "about_desc": f"Navigating the administrative landscape in Dubai requires precision. Our dedicated experts handle every technicality of your {title}, ensuring 100% compliance with local laws, incredibly fast turnaround times, and total peace of mind.",
        "requirements": content["requirements"],
        "steps": content["steps"]
    }

services = [
    # Card 1: Business Setup & Licensing
    make_service("New Company Incorporation", "new-company-incorporation.html", "business-setup-licensing.html", "Business Setup"),
    make_service("Branch Office Setup", "branch-office-setup.html", "business-setup-licensing.html", "Business Setup"),
    make_service("Subsidiary Company Formation", "subsidiary-company-formation.html", "business-setup-licensing.html", "Business Setup"),
    make_service("Civil Company Formation", "civil-company-formation.html", "business-setup-licensing.html", "Business Setup"),
    make_service("Sole Establishment Setup", "sole-establishment-setup.html", "business-setup-licensing.html", "Business Setup"),
    make_service("Partnership Company Formation", "partnership-company-formation.html", "business-setup-licensing.html", "Business Setup"),
    make_service("LLC Company Formation", "llc-company-formation.html", "business-setup-licensing.html", "Business Setup"),
    make_service("Trade License Issuance", "trade-license-issuance.html", "business-setup-licensing.html", "Business Setup"),
    make_service("License Amendment Services", "license-amendment-services.html", "business-setup-licensing.html", "Business Setup"),
    make_service("License Activity Addition / Removal", "license-activity-addition.html", "business-setup-licensing.html", "Business Setup"),
    make_service("Instant License Processing", "instant-license-processing.html", "business-setup-licensing.html", "Business Setup"),
    make_service("E-Commerce License Setup", "ecommerce-license-setup.html", "business-setup-licensing.html", "Business Setup", "indigo"),
    make_service("Professional License Setup", "professional-license-setup.html", "business-setup-licensing.html", "Business Setup"),
    make_service("Commercial License Setup", "commercial-license-setup.html", "business-setup-licensing.html", "Business Setup"),
    make_service("Industrial License Setup", "industrial-license-setup.html", "business-setup-licensing.html", "Business Setup", "indigo"),

    # Card 2: Free Zone & Offshore
    make_service("Free Zone License Renewal", "freezone-license-renewal.html", "freezone-offshore.html", "Free Zone & Offshore", "emerald"),
    make_service("Offshore Company Registration", "offshore-company-registration.html", "freezone-offshore.html", "Free Zone & Offshore", "emerald"),
    make_service("Offshore Bank Account Assistance", "offshore-bank-account.html", "freezone-offshore.html", "Free Zone & Offshore", "emerald"),
    
    # Card 3: Visa & Immigration
    make_service("Investor Visa Services", "investor-visa.html", "visa-immigration.html", "Visa & Immigration", "purple"),
    make_service("Employment Visa Processing", "employment-visa.html", "visa-immigration.html", "Visa & Immigration", "purple"),
    make_service("Family Visa Sponsorship", "family-visa.html", "visa-immigration.html", "Visa & Immigration", "purple"),
    make_service("Visa Renewal Services", "visa-renewal.html", "visa-immigration.html", "Visa & Immigration", "purple"),
    make_service("Visa Cancellation Services", "visa-cancellation.html", "visa-immigration.html", "Visa & Immigration", "purple"),
    make_service("Entry Permit Processing", "entry-permit.html", "visa-immigration.html", "Visa & Immigration", "purple"),
    make_service("Status Change Services", "status-change.html", "visa-immigration.html", "Visa & Immigration", "purple"),
    make_service("Medical Test Appointment Services", "medical-test.html", "visa-immigration.html", "Visa & Immigration", "purple"),
    make_service("Emirates ID Application", "emirates-id.html", "visa-immigration.html", "Visa & Immigration", "purple"),
    
    # Card 4: PRO & Government
    make_service("Government Approvals & Clearances", "government-approvals.html", "pro-government.html", "PRO & Government", "amber"),
    make_service("Labor & Immigration Services", "labor-immigration.html", "pro-government.html", "PRO & Government", "amber"),
    make_service("MOA Drafting & Notarization", "moa-drafting.html", "pro-government.html", "PRO & Government", "amber"),
    make_service("Power of Attorney Processing", "power-of-attorney.html", "pro-government.html", "PRO & Government", "amber"),
    make_service("Legal Document Typing Services", "legal-document-typing.html", "pro-government.html", "PRO & Government", "amber"),
    make_service("Document Attestation Services", "document-attestation.html", "pro-government.html", "PRO & Government", "amber"),
    make_service("Court & Notary Services", "court-notary.html", "pro-government.html", "PRO & Government", "amber"),
    
    # Card 5: Corporate & Admin
    make_service("VAT Registration & Filing", "vat-registration.html", "corporate-admin.html", "Corporate & Administrative", "rose"),
    make_service("Corporate Tax Registration", "corporate-tax.html", "corporate-admin.html", "Corporate & Administrative", "rose"),
    make_service("Audit Assistance", "audit-assistance.html", "corporate-admin.html", "Corporate & Administrative", "rose"),
    make_service("Business Advisory Services", "business-advisory.html", "corporate-admin.html", "Corporate & Administrative", "rose"),
    make_service("Company Restructuring", "company-restructuring.html", "corporate-admin.html", "Corporate & Administrative", "rose"),
    make_service("Share Transfer Services", "share-transfer.html", "corporate-admin.html", "Corporate & Administrative", "rose"),
    make_service("Company Liquidation", "company-liquidation.html", "corporate-admin.html", "Corporate & Administrative", "rose"),
    
    # Card 6: Office & Business Support
    make_service("Office Space Leasing Assistance", "office-space-leasing.html", "office-business-support.html", "Office & Business Support", "cyan"),
    make_service("Virtual Office Services", "virtual-office.html", "office-business-support.html", "Office & Business Support", "cyan"),
    make_service("Flexi Desk Solutions", "flexi-desk.html", "office-business-support.html", "Office & Business Support", "cyan"),
    make_service("Ejari Registration", "ejari-registration.html", "office-business-support.html", "Office & Business Support", "cyan"),
    make_service("Business Center Services", "business-center.html", "office-business-support.html", "Office & Business Support", "cyan"),
    
    # Card 7: Branding & Expansion
    make_service("Brand Name Registration", "brand-name-registration.html", "branding-expansion.html", "Branding & Expansion", "teal"),
    make_service("Website Development Support", "website-development.html", "branding-expansion.html", "Branding & Expansion", "teal"),
    make_service("Digital Marketing Assistance", "digital-marketing.html", "branding-expansion.html", "Branding & Expansion", "teal"),
    make_service("Business Growth Consulting", "business-growth-consulting.html", "branding-expansion.html", "Branding & Expansion", "teal"),
    make_service("Market Entry Strategy Consulting", "market-entry-strategy.html", "branding-expansion.html", "Branding & Expansion", "teal"),
]

with open('services_data.json', 'w') as f:
    json.dump(services, f, indent=4)
print("Created sophisticated services_data.json")
