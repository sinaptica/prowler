# Prowler App

**Prowler App** is a user-friendly interface for Prowler CLI, providing a visual dashboard to monitor your cloud security posture. This tutorial will guide you through setting up and using Prowler App.

## Accessing Prowler App and API Documentation

After [installing](../index.md#prowler-app-installation) **Prowler App**, access it at [http://localhost:3000](http://localhost:3000). To view the auto-generated **Prowler API** documentation, navigate to [http://localhost:8080/api/v1/docs](http://localhost:8080/api/v1/docs). This documentation provides details on available endpoints, parameters, and responses.

???+ note
    If you are a [Prowler Cloud](https://cloud.prowler.com/sign-in) user, you can access API docs at [https://api.prowler.com/api/v1/docs](https://api.prowler.com/api/v1/docs)

## **Step 1: Sign Up**

### **Sign Up with Email**

To get started, sign up using your email and password:

<img src="../../img/sign-up-button.png" alt="Sign Up Button" width="320"/>
<img src="../../img/sign-up.png" alt="Sign Up" width="285"/>

### **Sign Up with Social Login**

If Social Login is enabled, you can sign up using your preferred provider (e.g., Google, GitHub).

???+ note "How Social Login Works"
    If your email is already registered, you will be logged in, and your social account will be linked.
    If your email is not registered, a new account will be created using your social account email.

???+ note "Enable Social Login"
    See [how to configure Social Login for Prowler](prowler-app-social-login.md) to enable this feature in your own deployments.

## **Step 2: Log In**

Once registered, log in with your email and password to access Prowler App.

<img src="../../img/log-in.png" alt="Log In" width="350"/>

Upon logging in, the Overview page will display. At this stage, no data is present: add a provider to begin scanning your cloud environment.

## **Step 3: Add a Provider**

To perform security scans, link a cloud provider account. Prowler supports the following providers:

- **AWS**

- **Azure**

- **Google Cloud Platform (GCP)**

- **Kubernetes**

- **M365**

Steps to add a provider:

1. Navigate to `Settings > Cloud Providers`.
2. Click `Add Account` to set up a new provider and provide your credentials.

<img src="../../img/add-provider.png" alt="Add Provider" width="700"/>

## **Step 4: Configure the Provider**

Select the cloud provider you want to scan.

<img src="../../img/select-provider.png" alt="Select a Provider" width="700"/>

Once chosen, enter the Provider UID for authentication:

- **AWS**: Enter your AWS Account ID.
- **GCP**: Enter your GCP Project ID.
- **Azure**: Enter your Azure Subscription ID.
- **Kubernetes**: Enter your Kubernetes Cluster context of your kubeconfig file.
- **M365**: Enter your M365 Domain ID.

Optionally, provide a **Provider Alias** for easier identification. Follow the instructions provided to add your credentials:

### **Step 4.1: AWS Credentials**

For AWS, enter your `AWS Account ID` and choose one of the following methods to connect:

#### **Step 4.1.1: IAM Access Keys**

1. Select `Connect via Credentials`.

    <img src="../../img/connect-aws-credentials.png" alt="AWS Credentials" width="350"/>

2. Enter your `Access Key ID`, `Secret Access Key` and optionally a `Session Token`:

    <img src="../../img/aws-credentials.png" alt="AWS Credentials" width="350"/>

#### **Step 4.1.2: IAM Role**

1. Select `Connect assuming IAM Role`.

    <img src="../../img/connect-aws-role.png" alt="AWS Role" width="350"/>

2. Enter the `Role ARN` and any optional field like the AWS Access Keys to assume the role, the `External ID`, the `Role Session Name` or the `Session Duration`:

    <img src="../../img/aws-role.png" alt="AWS Role" width="700"/>

???+ note
    Check if your AWS Security Token Service (STS) has the EU (Ireland) endpoint active. If not, we will not be able to connect to your AWS account.

    If that is the case your STS configuration may look like this:

    <img src="../../img/sts-configuration.png" alt="AWS Role" width="800"/>

    To solve this issue, please activate the EU (Ireland) STS endpoint.

### **Step 4.2: Azure Credentials**:

For Azure, Prowler App uses a service principal application to authenticate. For more information about the process of creating and adding permissions to a service principal refer to this [section](../getting-started/requirements.md#azure). When you finish creating and adding the [Entra](./azure/create-prowler-service-principal.md#assigning-the-proper-permissions) and [Subscription](./azure/subscriptions.md#assign-the-appropriate-permissions-to-the-identity-that-is-going-to-be-assumed-by-prowler) scope permissions to the service principal, enter the `Tenant ID`, `Client ID` and `Client Secret` of the service principal application.

<img src="../../img/azure-credentials.png" alt="Azure Credentials" width="700"/>

---
### **Step 4.3: GCP Credentials**

For Google Cloud, first enter your `GCP Project ID` and then select the authentication method you want to use:

- **Service Account Authentication** (**Recommended**)
- **Application Default Credentials**

**Service Account Authentication** is the recommended authentication method for automated systems and machine-to-machine interactions, like Prowler. For detailed information about this, refer to the [Google Cloud documentation](https://cloud.google.com/iam/docs/service-account-overview).

<img src="../img/gcp-auth-methods.png" alt="GCP Authentication Methods" width="700"/>

#### **Step 4.3.1: Service Account Authentication**

First of all, in the same project that you selected in the previous step, you need to create a service account and then generate a key in JSON format for it. For more information about this, you can follow the next Google Cloud documentation tutorials:

- [Create a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts)
- [Generate a key for a service account](https://cloud.google.com/iam/docs/creating-managing-service-account-keys)

<img src="../img/gcp-service-account-creds.png" alt="GCP Service Account Credentials" width="700"/>

#### **Step 4.3.2: Application Default Credentials**

1. Run the following command in your terminal to authenticate with GCP:

    ```bash
    gcloud auth application-default login
    ```

2. Once authenticated, get the `Client ID`, `Client Secret` and `Refresh Token` from `~/.config/gcloud/application_default_credentials`.

3. Paste the `Client ID`, `Client Secret` and `Refresh Token` into Prowler App.

<img src="../../img/gcp-credentials.png" alt="GCP Credentials" width="700"/>

### **Step 4.4: Kubernetes Credentials**:

For Kubernetes, Prowler App uses a `kubeconfig` file to authenticate, paste the contents of your `kubeconfig` file into the `Kubeconfig content` field.

By default, the `kubeconfig` file is located at `~/.kube/config`.

<img src="../../img/kubernetes-credentials.png" alt="Kubernetes Credentials" width="700"/>

If you are adding an **EKS**, **GKE**, **AKS** or external cluster, follow these additional steps to ensure proper authentication:

**Make sure your cluster allow traffic from the Prowler Cloud IP address `52.48.254.174/32`**

1. Apply the necessary Kubernetes resources to your EKS, GKE, AKS or external cluster (you can find the files in the [`kubernetes` directory of the Prowler repository](https://github.com/prowler-cloud/prowler/tree/master/kubernetes)):

    ```console
    kubectl apply -f kubernetes/prowler-sa.yaml
    kubectl apply -f kubernetes/prowler-role.yaml
    kubectl apply -f kubernetes/prowler-rolebinding.yaml
    ```

2. Generate a long-lived token for authentication:

    ```console
    kubectl create token prowler-sa -n prowler-ns --duration=0
    ```

    - **Security Note:** The `--duration=0` option generates a non-expiring token, which may pose a security risk if not managed properly. Users should decide on an appropriate expiration time based on their security policies. If a limited-time token is preferred, set `--duration=<TIME>` (e.g., `--duration=24h`).
    - **Important:** If the token expires, Prowler Cloud will no longer be able to authenticate with the cluster. In this case, you will need to generate a new token and **remove and re-add the provider in Prowler Cloud** with the updated `kubeconfig`.

3. Update your `kubeconfig` to use the ServiceAccount token:

    ```console
    kubectl config set-credentials prowler-sa --token=<SA_TOKEN>
    kubectl config set-context <CONTEXT_NAME> --user=prowler-sa
    ```

    Replace `<SA_TOKEN>` with the generated token and `<CONTEXT_NAME>` with your KubeConfig Context Name of your EKS, GKE or AKS cluster.

4. Now you can add the modified `kubeconfig` in Prowler Cloud. Then test the connection.

### **Step 4.5: M365 Credentials**
For M365, you must enter your Domain ID and choose the authentication method you want to use:

- Service Principal Authentication (Recommended)
- User Authentication (only works if the user does not have MFA enabled)

???+ note
    User authentication with M365_USER and M365_PASSWORD is optional and will only work if the account does not enforce MFA.

For full setup instructions and requirements, check the [Microsoft 365 provider requirements](./microsoft365/getting-started-m365.md).

<img src="../../img/m365-credentials.png" alt="Prowler Cloud M365 Credentials" width="700"/>

## **Step 5: Test Connection**

After adding your credentials of your cloud account, click the `Launch` button to verify that Prowler App can successfully connect to your provider:

<img src="../../img/test-connection-button.png" alt="Test Connection" width="700"/>

## **Step 6: Scan started**

After successfully adding and testing your credentials, Prowler will start scanning your cloud environment, click the `Go to Scans` button to see the progress:

<img src="../../img/provider-added.png" alt="Start Now" width="700"/>

???+ note
    Prowler will automatically scan all configured providers every **24 hours**, ensuring your cloud environment stays continuously monitored.

## **Step 7: Monitor Scan Progress**

Track the progress of your scan in the `Scans` section:

<img src="../../img/scan-progress.png" alt="Scan Progress" width="700"/>


## **Step 8: Analyze the Findings**

While the scan is running, start exploring the findings in these sections:

- **Overview**: High-level summary of the scans.

    <img src="../../img/overview.png" alt="Overview" width="700"/>

- **Compliance**: Insights into compliance status.

    <img src="../../img/compliance.png" alt="Compliance" width="700"/>

- **Issues**: Types of issues detected.

    <img src="../../img/issues.png" alt="Issues" width="300" style="text-align: center;"/>

- **Browse All Findings**: Detailed list of findings detected, where you can filter by severity, service, and more.

    <img src="../../img/findings.png" alt="Findings" width="700"/>

To view all `new` findings that have not been seen prior to this scan, click the `Delta` filter and select `new`. To view all `changed` findings that have had a status change (from `PASS` to `FAIL` for example), click the `Delta` filter and select `changed`.

## **Step 9: Download the Outputs**

Once a scan is complete, navigate to the Scan Jobs section to download the output files generated by Prowler:

<img src="../../img/scan_jobs_section.png" alt="Scan Jobs section" width="700"/>

You can download the output files generated by Prowler as a single `zip` file. This archive contains the CSV, JSON-OSCF, and HTML reports detailing the findings.

To download these files, click the **Download** button. This button becomes available only after the scan has finished.

<img src="../../img/download_output.png" alt="Download output" width="700"/>

The `zip` file unpacks into a folder named like `prowler-output-<provider_id>-<timestamp>`, which includes all of the above outputs. In the example below, you can see the `.csv`, .`json`, and `.html` reports alongside a subfolder for detailed compliance checks.

<img src="../../img/output_folder.png" alt="Output folder" width="700"/>

???+ note "API Note"
    For more information about the API endpoint used by the UI to download the ZIP archive, refer to: [Prowler API Reference - Download Scan Output](https://api.prowler.com/api/v1/docs#tag/Scan/operation/scans_report_retrieve)

## **Step 10: Download specified compliance report**

Once your scan has finished, you don’t need to grab the entire ZIP—just pull down the specific compliance report you want:

- Navigate to the **Compliance** section of the UI.

<img src="../../img/compliance_section.png" alt="Compliance section" width="700"/>

- Find the Framework report you need.

- Click its **Download** icon to retrieve that report’s CSV file with all the detailed findings.

<img src="../../img/compliance_download.png" alt="Download compliance output" width="700"/>

???+ note "API Note"
    To fetch a single compliance report via API, see the Retrieve compliance report as CSV endpoint in the Prowler API Reference.[Prowler API Reference - Retrieve compliance report as CSV](https://api.prowler.com/api/v1/docs#tag/Scan/operation/scans_compliance_retrieve)
