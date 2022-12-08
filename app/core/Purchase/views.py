from __future__ import print_function
from django.http import QueryDict
from django.shortcuts import redirect, render
from .models import Contract,Department
from account.models import Account
from mailmerge import MailMerge
from datetime import date
from Purchase.models import Contract,ContractType, Currency, PaymentTerms, TerminationTerms, Status
import datetime
from django.contrib.auth import authenticate 
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user
from django.contrib import messages
from django.core.mail import send_mail


def send_mail_main(request):
    send_mail("salam","message","ulvi@elab.az",["ulvi.allahverdiyev@fairmont.com"],fail_silently=True)
    return redirect("home")

def login(request):
    if request.user.is_authenticated:
        return render(request,"home.html")
    else:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login_user(request, user)
                return redirect("home")
            else:
                messages.warning(request, 'You have not entered the correct username or password.')
                return redirect("login")
        return render(request,"auth-signin.html")

def logout(request):
    logout_user(request)
    return redirect("login")


def homepage(request):
    contracts = Contract.objects.all().count()
    con_approved = Contract.objects.filter(approval_status=5).count()
    if request.user.is_authenticated:
        context = {
            "cons":contracts,
            "con_approved":con_approved,
        }
        return render(request,"home.html",context=context)
    else:
       return redirect("login")
    

def purchase_contract_list(request):
    accounts_data = Account.objects.get(id=request.user.id)
    account = list()
    count = len(accounts_data.allowed_departments)
    for i in range(count):
        account.append(int(accounts_data.allowed_departments[i]))
    all_contracts = Contract.objects.all()
    context = {
        'all_contracts':all_contracts,
        'account':account,
    }
    return render(request,"purchase-contract-list.html",context=context)

def delete_contract(request,id):
    get_status = Contract.objects.get(contract_id=id).delete()
    return redirect("purchase_contract_list")

def reject(request,id):
    if request.method == "POST":
        get_status = Contract.objects.get(contract_id=id)
        comment = request.POST["rejection_comment"]
        get_status.approval_status = 0
        get_status.reject_comment = comment
        get_status.creator_edit = True
        get_status.save()
        return redirect("home")
    contract = Contract.objects.get(contract_id=id)
    context = {
        "contract":contract,
    }
    return render(request,"pre-reject.html",context=context)
    

def approve(request,id):
    get_status = Contract.objects.get(contract_id=id)
    get_status.approval_status +=1
    get_status.creator_edit = False
    get_status.save()
    
    if get_status.approval_status == 5:
        if get_status.contract_type.name == "Purchase":
            template = "contracts/purchase_template.docx"
            document = MailMerge(template)
            document.merge(
                contract_number = get_status.contract_id,
                contract_date = str(get_status.start_date),
                vendor_director = str(get_status.vendor_director),
                vendor_name = get_status.vendor_name,
                payment_name = get_status.payment_terms.name,
                end_date = str(get_status.end_date),
                termination_term = get_status.termination_terms.name,
                vendor_voen = str(get_status.vendor_voen),
                vendor_address = get_status.vendor_address,
                vendor_email = get_status.vendor_email,
                vendor_phone = get_status.vendor_phone,
                bank_name = get_status.bank_name,
                bank_voen = str(get_status.bank_voen),
                bank_code = str(get_status.bank_code),
                bank_swift = str(get_status.bank_swift),
                bank_mh = get_status.bank_m_h,
                bank_hh = get_status.bank_h_h,
                director_name = get_status.vendor_director,
                company_name = get_status.vendor_name
            )
            document.write("static/exported/" + "Purchase_" + str(get_status.contract_id) + ".docx")
            get_status.contract_exported_link = "static/exported/"  + "Purchase_" + str(get_status.contract_id) + ".docx"
            get_status.save()
            document.close()
            return redirect("home")
        elif get_status.contract_type.name == "Service":
            template = "contracts/service_contract.docx"
            document = MailMerge(template)
            document.merge(
                contract_number = get_status.contract_id,
                contract_date = str(get_status.start_date),
                vendor_director = str(get_status.vendor_director),
                vendor_name = get_status.vendor_name,
                payment_name = get_status.payment_terms.name,
                end_date = str(get_status.end_date),
                termination_term = get_status.termination_terms.name,
                vendor_voen = str(get_status.vendor_voen),
                vendor_address = get_status.vendor_address,
                vendor_email = get_status.vendor_email,
                vendor_phone = get_status.vendor_phone,
                bank_name = get_status.bank_name,
                bank_voen = str(get_status.bank_voen),
                bank_code = str(get_status.bank_code),
                bank_swift = str(get_status.bank_swift),
                bank_mh = get_status.bank_m_h,
                bank_hh = get_status.bank_h_h,
                director_name = get_status.vendor_director,
                company_name = get_status.vendor_name
                
            )
            document.write("static/exported/" + "Service_" + str(get_status.contract_id) + ".docx")
            get_status.contract_exported_link = "static/exported/" + "Service_" + str(get_status.contract_id) + ".docx"
            get_status.save()
            document.close()
            return redirect("home")
        elif get_status.contract_type.name == "InternationalSupplier":
            template = "contracts/international_suppliers.docx"
            document = MailMerge(template)
            document.merge(
                contract_number = get_status.contract_id,
                contract_date = str(get_status.start_date),
                vendor_director = str(get_status.vendor_director),
                vendor_name = get_status.vendor_name,
                payment_name = get_status.payment_terms.name,
                end_date = str(get_status.end_date),
                termination_term = get_status.termination_terms.name,
                vendor_voen = str(get_status.vendor_voen),
                vendor_address = get_status.vendor_address,
                vendor_email = get_status.vendor_email,
                vendor_phone = get_status.vendor_phone,
                bank_name = get_status.bank_name,
                bank_voen = str(get_status.bank_voen),
                bank_code = str(get_status.bank_code),
                bank_swift = str(get_status.bank_swift),
                bank_mh = get_status.bank_m_h,
                bank_hh = get_status.bank_h_h,
                director_name = get_status.vendor_director,
                company_name = get_status.vendor_name
                
            )
            document.write("static/exported/" + "Service_" + str(get_status.contract_id) + ".docx")
            get_status.contract_exported_link = "static/exported/" + "InternationalSuppliers_" + str(get_status.contract_id) + ".docx"
            get_status.save()
            document.close()
            return redirect("purchase_contract_list")
    return redirect("home")



def purchase_contract_add(request):
    if request.method == "POST":
        end_date = request.POST['end_date']
        account_number = request.POST['account_number']
        contract_type = request.POST['contract_type']
        department = request.POST['department']
        deparment_instance = Department.objects.get(id=department)
        currency = request.POST['currency']
        currencies = Currency.objects.all()
        contract_value = request.POST['contract_value']
        percentage = request.POST['percentage']
        vendor_code = request.POST['vendor_code']
        termination_terms = request.POST['termination_terms']
        payment_terms = request.POST['payment_terms']
        vendor_phone = request.POST['vendor_phone']
        vendor_email = request.POST['vendor_email']
        description = request.POST['description']
        vendor_name = request.POST['vendor_name']
        vendor_director = request.POST['vendor_director']
        vendor_voen = request.POST['vendor_voen']
        vendor_address = request.POST['vendor_address']
        bank_name = request.POST['bank_name']
        bank_voen = request.POST['bank_voen']
        bank_code = request.POST['bank_code']
        bank_swift = request.POST['bank_swift']
        bank_m_h = request.POST['bank_m_h']
        bank_h_h = request.POST['bank_h_h']
        user = request.user
        if len(deparment_instance.name) > 2:
            contract_id = str(deparment_instance.name[:3]).upper() + str("00") + str(deparment_instance.count+1)
            deparment_instance.count+=1
            deparment_instance.save()
        else:
            contract_id = str(deparment_instance.name[:2]).upper() + str("00") + str(deparment_instance.count+1)
            deparment_instance.count+=1
            deparment_instance.save()
        year = end_date[:4]
        month = end_date[5:7]
        if month.startswith("0"):
            month = month.replace("0","")
        day = end_date[8:10]
        if day.startswith("0"):
            day = day.replace("0","")
        end_date = datetime.datetime(int(year),int(month),int(day),0,0)
        currency_instance = Currency.objects.get(id=currency)
        type_instance = ContractType.objects.get(id=contract_type)
        payment_terms_instance = PaymentTerms.objects.get(id=payment_terms)
        termination_terms_instance = TerminationTerms.objects.get(id=termination_terms)
        status_instance = Status.objects.get(id=1)
        new_contract = Contract(user=user,contract_id=contract_id,vendor_code=vendor_code,contract_type=type_instance,end_date=end_date,description=description,payment_terms=payment_terms_instance,termination_terms=termination_terms_instance,status=status_instance,account_number=account_number, currency=currency_instance, approval_status = 0, contract_value=contract_value,percentage=percentage,department=deparment_instance, vendor_email=vendor_email,vendor_phone=vendor_phone,vendor_director=vendor_director,vendor_name=vendor_name,vendor_voen=vendor_voen,vendor_address=vendor_address, bank_name=bank_name, bank_voen=bank_voen, bank_code=bank_code,bank_swift=bank_swift,bank_m_h=bank_m_h, bank_h_h=bank_h_h)
        new_contract.save()
        context = {
            'contract_id': contract_id,
        }
        return render(request,"contract-added.html",context=context)

    else:
        departments = Department.objects.all()
        termination_terms = TerminationTerms.objects.all()
        payment_terms = PaymentTerms.objects.all()
        status = Status.objects.all()
        currencies = Currency.objects.all()
        types = ContractType.objects.all()
        context = {
            'departments':departments,
            'types':types,
            'currencies':currencies,
            'payment_terms':payment_terms,
            'termination_terms':termination_terms,
            'status':status,
        }
        return render(request,'purchase-contract-add.html',context=context)

def edit_contract(request,id):
    if request.method == "POST":
        end_date = request.POST['end_date']
        account_number = request.POST['account_number']
        contract_type = request.POST['contract_type']
        department = request.POST['department']
        deparment_instance = Department.objects.get(id=department)
        currency = request.POST['currency']
        currencies = Currency.objects.all()
        contract_value = request.POST['contract_value']
        vendor_code = request.POST['vendor_code']
        termination_terms = request.POST['termination_terms']
        payment_terms = request.POST['payment_terms']
        vendor_phone = request.POST['vendor_phone']
        vendor_email = request.POST['vendor_email']
        description = request.POST['description']
        vendor_name = request.POST['vendor_name']
        vendor_director = request.POST['vendor_director']
        vendor_voen = request.POST['vendor_voen']
        vendor_address = request.POST['vendor_address']
        bank_name = request.POST['bank_name']
        bank_voen = request.POST['bank_voen']
        bank_code = request.POST['bank_code']
        bank_swift = request.POST['bank_swift']
        bank_m_h = request.POST['bank_m_h']
        bank_h_h = request.POST['bank_h_h']
        if len(deparment_instance.name) > 2:
            contract_id = str(deparment_instance.name[:3]).upper() + str("00") + str(deparment_instance.count+1)
            deparment_instance.count+=1
            deparment_instance.save()
        else:
            contract_id = str(deparment_instance.name[:2]).upper() + str("00") + str(deparment_instance.count+1)
            deparment_instance.count+=1
            deparment_instance.save()
        year = end_date[:4]
        month = end_date[5:7]
        if month.startswith("0"):
            month = month.replace("0","")
        day = end_date[8:10]
        if day.startswith("0"):
            day = day.replace("0","")
        end_date = datetime.datetime(int(year),int(month),int(day),0,0)
        currency_instance = Currency.objects.get(id=currency)
        type_instance = ContractType.objects.get(id=contract_type)
        payment_terms_instance = PaymentTerms.objects.get(id=payment_terms)
        termination_terms_instance = TerminationTerms.objects.get(id=termination_terms)
        status_instance = Status.objects.get(id=1)
        new_contract = Contract.objects.filter(contract_id=id).update(vendor_code=vendor_code,contract_type=type_instance,end_date=end_date,description=description,payment_terms=payment_terms_instance,termination_terms=termination_terms_instance,status=status_instance,account_number=account_number, currency=currency_instance, approval_status = 0, contract_value=contract_value,department=deparment_instance, vendor_email=vendor_email,vendor_phone=vendor_phone,vendor_director=vendor_director,vendor_name=vendor_name,vendor_voen=vendor_voen,vendor_address=vendor_address, bank_name=bank_name, bank_voen=bank_voen, bank_code=bank_code,bank_swift=bank_swift,bank_m_h=bank_m_h, bank_h_h=bank_h_h)
        context = {
            'contract_id': contract_id,
        }
        return redirect("purchase_contract_list")
    else:
        contract = Contract.objects.get(contract_id=id)
        departments = Department.objects.all().exclude(id=contract.department.id)
        termination_terms = TerminationTerms.objects.all().exclude(id=contract.termination_terms.id)
        payment_terms = PaymentTerms.objects.all().exclude(id=contract.payment_terms.id)
        status = Status.objects.all()
        currencies = Currency.objects.all().exclude(id=contract.currency.id)
        types = ContractType.objects.all().exclude(id=contract.contract_type.id)
        end_date = contract.end_date.isoformat()[:10]
        context = {
            'contract':contract,
            'departments':departments,
            'types':types,
            'currencies':currencies,
            'payment_terms':payment_terms,
            'termination_terms':termination_terms,
            'status':status,
            'end_date':end_date,
        }
        return render(request,"edit_contract.html",context=context)