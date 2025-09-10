import React, { useMemo, useState } from "react";

/* ========= Shared UI (defined OUTSIDE to avoid remounts) ========= */

function Header({ progressPct, title }) {
  return (
    <header className="w-full">
      <div className="mx-auto max-w-3xl px-4">
        <div className="flex items-center justify-between py-3">
          <div className="flex items-center gap-2">
            <div className="h-6 w-6 rounded-sm bg-red-600 border-2 border-yellow-400" />
            <span className="font-semibold text-black text-lg">
              College Park Apartment Portal
            </span>
          </div>
          <span className="text-xs font-medium text-neutral-600">Made for UMD students</span>
        </div>

        {/* PROGRESS BAR */}
        <div className="mt-2 w-full rounded-full bg-neutral-200 h-2 overflow-hidden">
          <div
            className="h-2 bg-red-600 rounded-full transition-[width] duration-500 ease-out"
            style={{ width: `${Math.max(0, Math.min(100, progressPct))}%` }}
            role="progressbar"
            aria-valuemin={0}
            aria-valuemax={100}
            aria-valuenow={Math.round(progressPct)}
            aria-label="Form progress"
          />
        </div>
        <div className="mt-1 text-xs text-neutral-600">
          {Math.round(Math.max(0, Math.min(100, progressPct)))}% complete
        </div>

        <div className="mt-2 text-sm font-semibold text-black">{title}</div>
      </div>
    </header>
  );
}


function Card({ children }) {
  return (
    <div className="w-full max-w-3xl rounded-2xl border border-umd-gold bg-white p-8 shadow-card">
      {children}
    </div>
  );
}

function PrimaryBtn({ children, ...props }) {
  return (
    <button
      className="inline-flex items-center justify-center rounded-2xl bg-red-600 px-6 py-3 text-white font-semibold shadow hover:bg-red-700 transition"
      {...props}
    >
      {children}
    </button>
  );
}


function SecondaryBtn({ children, ...props }) {
  return (
    <button
      className="rounded-2xl border border-black px-6 py-2 font-medium text-black transition hover:bg-black hover:text-white"
      {...props}
    >
      {children}
    </button>
  );
}

/* =================== App =================== */

// ---- Constants ----
const MIN_BUDGET = {
  "Terrapin Row": 1250,
  "University View": 1200,
  "The Varsity": 1104,
  "South Campus Commons": 1016,
};

const MAJOR_CATEGORIES = {
  1: "STEM",
  2: "Business",
  3: "Public Policy",
  4: "Fine Arts",
  5: "Architecture",
};

const MAJOR_TO_APARTMENTS = {
  1: ["University View", "The Varsity"],
  2: ["Terrapin Row", "South Campus Commons"],
  3: ["Terrapin Row", "South Campus Commons"],
  4: ["University View", "The Varsity"],
  5: ["Terrapin Row", "South Campus Commons"],
};

const MAJOR_PROXIMITY_TEXT = {
  1: "University View and The Varsity are located near STEM buildings.",
  2: "Terrapin Row and South Campus Commons are located near Business buildings.",
  3: "Terrapin Row and South Campus Commons are located near Public Policy buildings.",
  4: "University View and The Varsity are located near Fine Arts buildings.",
  5: "Terrapin Row and South Campus Commons are located near Architecture buildings.",
};

const EMAIL_REGEX = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
const PHONE_REGEX = /^\d{3}-\d{3}-\d{4}$/;
const NAME_REGEX = /[A-Za-z]\S+ .+?[A-Za-z\d]+$/;

export default function ApartmentPortal() {
  // step: 0=Welcome, 1=Eligibility, 2=Major, 3=Budget, 4=Choose, 5=Apply, 6=ThankYou
  const [step, setStep] = useState(0);

  // Eligibility
  const [fullName, setFullName] = useState("");
  const [hasID, setHasID] = useState("no");
  const [hasIncome, setHasIncome] = useState("no");
  const eligible = hasID === "yes" && hasIncome === "yes";

  // Major & apartments
  const [majorCategory, setMajorCategory] = useState(1);
  const apartmentsForMajor = useMemo(
    () => MAJOR_TO_APARTMENTS[majorCategory],
    [majorCategory]
  );

  // Budget
  const [minBudgetInput, setMinBudgetInput] = useState("");
  const [affordabilityMsg, setAffordabilityMsg] = useState(null);

  // Choice & group
  const [chosenApartment, setChosenApartment] = useState(null);
  const [moveWithOthers, setMoveWithOthers] = useState("n");
  const [numPeople, setNumPeople] = useState(""); // allow blank

  // Application
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");

  const stepTitles = [
    "Welcome",
    "Eligibility",
    "Major & Proximity",
    "Budget",
    "Choose Apartment & Group",
    "Application",
    "All Set!",
  ];
  const progressPct = (Math.min(step, 6) / 6) * 100;

  // Handlers
  const handleBudgetCheck = () => {
    const [apt1, apt2] = apartmentsForMajor;
    const b = Number(minBudgetInput);
    if (Number.isNaN(b)) return setAffordabilityMsg("Please enter a valid number.");

    const a1Min = MIN_BUDGET[apt1];
    const a2Min = MIN_BUDGET[apt2];
    const cheapestVal = Math.min(a1Min, a2Min);
    const cheapestName =
      Object.entries(MIN_BUDGET).find(([, v]) => v === cheapestVal)?.[0] ?? "";

    if (b >= a1Min && b >= a2Min) {
      setAffordabilityMsg(
        `You can afford both ${apt1} and ${apt2}. The cheapest is ${cheapestName} ($${cheapestVal}).`
      );
    } else if (b >= a1Min) {
      setAffordabilityMsg(`You can afford ${apt1} only.`);
    } else if (b >= a2Min) {
      setAffordabilityMsg(`You can afford ${apt2} only.`);
    } else {
      setAffordabilityMsg("You cannot afford either apartment.");
    }
  };

  const handleStep4Continue = () => {
    if (!chosenApartment) {
      alert("Please choose an apartment.");
      return;
    }
    if (moveWithOthers === "y") {
      const n = Number(numPeople);
      if (!numPeople || Number.isNaN(n) || n < 1 || n > 4) {
        alert("Enter a valid group size (1–4).");
        return;
      }
    }
    setStep(5);
  };

  const handleApplicationSubmit = () => {
    const nameOk = NAME_REGEX.test(fullName);
    const emailOk = EMAIL_REGEX.test(email);
    const phoneOk = PHONE_REGEX.test(phone);

    if (!nameOk) return alert("Invalid name. Please enter a first and last name.");
    if (!emailOk) return alert("Invalid email.");
    if (!phoneOk) return alert("Invalid phone number. Use format xxx-xxx-xxxx.");
    if (!username || username.length > 9) return alert("Username required (max 9 characters).");
    if (!chosenApartment) return alert("Please choose an apartment.");

    setStep(6); // thank-you page
  };

  return (
    <div className="min-h-screen bg-neutral-50 text-black">
      <Header progressPct={progressPct} title={stepTitles[step] || ""} />

      {/* Center every page vertically & horizontally */}
      <main className="mx-auto flex min-h-[calc(100vh-110px)] w-full max-w-3xl items-center justify-center px-4 py-12">
        {/* Step 0: Welcome */}
        {/* Step 0: Welcome */}
        {step === 0 && (
          <Card>
            <h1 className="text-3xl font-extrabold">Welcome!</h1>
            <p className="mt-3 text-neutral-700">
              This portal will guide you through choosing an apartment in College Park.
              You’ll answer a few quick questions — <span className="font-semibold">one page at a time</span>.
            </p>
            <ul className="mt-5 list-disc pl-6 text-sm text-neutral-800 space-y-1">
              <li>Verify eligibility</li>
              <li>Select your major area to see nearby apartments</li>
              <li>Check your budget</li>
              <li>Choose an apartment and (optionally) your group size</li>
              <li>Submit your application</li>
            </ul>

            {/* BUTTONS */}
            <div className="mt-8 flex w-full items-center justify-end gap-3">
              <button
                className="inline-flex items-center justify-center rounded-2xl border border-black px-6 py-3 font-medium text-black hover:bg-black hover:text-white transition"
                onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
              >
                Back to top
              </button>
              <PrimaryBtn onClick={() => setStep(1)}>Start</PrimaryBtn>
            </div>
          </Card>
        )}


        {/* Step 1: Eligibility */}
        {step === 1 && (
          <Card>
            <h2 className="text-xl font-bold">Step 1: Eligibility</h2>
            <div className="mt-4 grid gap-3">
              <input
                className="rounded-xl border border-neutral-300 px-3 py-2"
                placeholder="Full name"
                value={fullName}
                onChange={(e) => setFullName(e.target.value)}
              />
              <select
                className="rounded-xl border border-neutral-300 px-3 py-2"
                value={hasID}
                onChange={(e) => setHasID(e.target.value)}
              >
                <option value="no">Do you have ID? (no)</option>
                <option value="yes">Do you have ID? (yes)</option>
              </select>
              <select
                className="rounded-xl border border-neutral-300 px-3 py-2"
                value={hasIncome}
                onChange={(e) => setHasIncome(e.target.value)}
              >
                <option value="no">Proof of income? (no)</option>
                <option value="yes">Proof of income? (yes)</option>
              </select>
            </div>
            <div className="mt-6 flex items-center justify-between">
              <SecondaryBtn onClick={() => setStep(0)}>Back</SecondaryBtn>
              <PrimaryBtn disabled={!eligible} onClick={() => setStep(2)}>
                Continue
              </PrimaryBtn>
            </div>
            {!eligible && (
              <p className="mt-3 text-sm text-umd-red">
                You must have ID and proof of income to proceed.
              </p>
            )}
          </Card>
        )}

        {/* Step 2: Major & Proximity */}
        {step === 2 && (
          <Card>
            <h2 className="text-xl font-bold">Step 2: Major & Proximity</h2>
            <div className="mt-4 flex flex-wrap gap-2">
              {Object.entries(MAJOR_CATEGORIES).map(([k, v]) => (
                <button
                  key={k}
                  onClick={() => setMajorCategory(Number(k))}
                  className={`rounded-2xl border px-3 py-2 text-sm transition ${
                    Number(k) === majorCategory
                      ? "bg-black text-white"
                      : "bg-white hover:bg-neutral-100"
                  }`}
                >
                  {v}
                </button>
              ))}
            </div>
            <p className="mt-4 text-sm text-neutral-700">
              {MAJOR_PROXIMITY_TEXT[majorCategory]}
            </p>
            <div className="mt-6 flex items-center justify-between">
              <SecondaryBtn onClick={() => setStep(1)}>Back</SecondaryBtn>
              <PrimaryBtn onClick={() => setStep(3)}>Continue</PrimaryBtn>
            </div>
          </Card>
        )}

        {/* Step 3: Budget */}
        {step === 3 && (
          <Card>
            <h2 className="text-xl font-bold">Step 3: Budget</h2>
            <div className="mt-4 grid gap-3">
              <input
                className="rounded-xl border border-neutral-300 px-3 py-2"
                placeholder="Enter minimum monthly budget (USD)"
                value={minBudgetInput}
                onChange={(e) => setMinBudgetInput(e.target.value)}
                inputMode="numeric"
              />
              <div className="flex flex-wrap gap-3">
                <PrimaryBtn onClick={handleBudgetCheck}>Check affordability</PrimaryBtn>
                <SecondaryBtn onClick={() => { setMinBudgetInput(""); setAffordabilityMsg(null); }}>
                  Reset
                </SecondaryBtn>
              </div>
              {affordabilityMsg && (
                <div className="rounded-xl border border-umd-gold bg-yellow-50 px-3 py-2 text-sm text-black">
                  {affordabilityMsg}
                </div>
              )}
            </div>
            <div className="mt-6 flex items-center justify-between">
              <SecondaryBtn onClick={() => setStep(2)}>Back</SecondaryBtn>
              <PrimaryBtn onClick={() => setStep(4)}>Continue</PrimaryBtn>
            </div>
          </Card>
        )}

        {/* Step 4: Choose Apartment & Group */}
        {step === 4 && (
          <Card>
            <h2 className="text-xl font-bold">Step 4: Choose Apartment & Group</h2>
            <div className="mt-4 flex flex-wrap gap-2">
              {apartmentsForMajor.map((a) => (
                <button
                  key={a}
                  onClick={() => setChosenApartment(a)}
                  className={`rounded-2xl border px-3 py-2 text-sm transition ${
                    chosenApartment === a
                      ? "bg-black text-white"
                      : "bg-white hover:bg-neutral-100"
                  }`}
                >
                  {a}
                </button>
              ))}
            </div>
            <div className="mt-4 grid gap-3">
              <select
                className="rounded-xl border border-neutral-300 px-3 py-2"
                value={moveWithOthers}
                onChange={(e) => setMoveWithOthers(e.target.value)}
              >
                <option value="n">Moving with others? (no)</option>
                <option value="y">Moving with others? (yes)</option>
              </select>
              {moveWithOthers === "y" && (
                <input
                  type="number"
                  min="1"
                  max="4"
                  className="rounded-xl border border-neutral-300 px-3 py-2"
                  placeholder="Number of tenants (1–4)"
                  value={numPeople}
                  onChange={(e) => setNumPeople(e.target.value)}
                />
              )}
            </div>
            <div className="mt-6 flex items-center justify-between">
              <SecondaryBtn onClick={() => setStep(3)}>Back</SecondaryBtn>
              <PrimaryBtn onClick={handleStep4Continue}>Continue</PrimaryBtn>
            </div>
          </Card>
        )}

        {/* Step 5: Application */}
        {step === 5 && (
          <Card>
            <h2 className="text-xl font-bold">Step 5: Application</h2>
            <div className="mt-4 grid gap-3">
              <input
                className="rounded-xl border border-neutral-300 px-3 py-2"
                placeholder="Username (max 9 chars)"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
              />
              <input
                className="rounded-xl border border-neutral-300 px-3 py-2"
                placeholder="Full name"
                value={fullName}
                onChange={(e) => setFullName(e.target.value)}
              />
              <input
                className="rounded-xl border border-neutral-300 px-3 py-2"
                placeholder="Email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
              <input
                className="rounded-xl border border-neutral-300 px-3 py-2"
                placeholder="Phone (xxx-xxx-xxxx)"
                value={phone}
                onChange={(e) => setPhone(e.target.value)}
              />
            </div>
            <div className="mt-6 flex items-center justify-between">
              <SecondaryBtn onClick={() => setStep(4)}>Back</SecondaryBtn>
              <PrimaryBtn onClick={handleApplicationSubmit}>Submit application</PrimaryBtn>
            </div>
          </Card>
        )}

        {/* Step 6: Thank You */}
        {step === 6 && (
          <Card>
            <div className="flex items-center gap-3">
              <div className="h-4 w-4 rounded-sm bg-umd-red border-2 border-umd-gold" />
              <h2 className="text-xl font-bold">All set!</h2>
            </div>
            <p className="mt-3">
              Thank you, <span className="font-semibold">{fullName}</span>, for submitting your
              application to <span className="font-semibold">{chosenApartment}</span>. We’ll contact you soon.
            </p>
            {moveWithOthers === "y" && numPeople && (
              <p className="mt-1">
                Group size: <span className="font-semibold">{numPeople}</span>
              </p>
            )}
            <div className="mt-6 flex items-center justify-end gap-3">
              <SecondaryBtn onClick={() => setStep(4)}>Back</SecondaryBtn>
              <PrimaryBtn
                onClick={() => {
                  // reset for a new application
                  setStep(0);
                  setFullName(""); setHasID("no"); setHasIncome("no");
                  setMajorCategory(1);
                  setMinBudgetInput(""); setAffordabilityMsg(null);
                  setChosenApartment(null); setMoveWithOthers("n"); setNumPeople("");
                  setUsername(""); setEmail(""); setPhone("");
                }}
              >
                Start new application
              </PrimaryBtn>
            </div>
          </Card>
        )}
      </main>
    </div>
  );
}
