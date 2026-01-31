# Kinship: Technical Master Plan

## 1. Project Overview
**Kinship** is a family management application designed to gamify chores, manage schedules, and streamline meal planning. 
* **Goal:** Create a premium, responsive, and easy-to-deploy application for family use.

---

## 2. Technology Stack

### Backend
* **Language:** Python 3.11+
* **Framework:** FastAPI (High performance, easy documentation)
* **Validation:** Pydantic (Data validation and settings management)
* **Package Manager:** `uv` (Extremely fast Python package installer and resolver)
* **Database ORM:** SQLAlchemy 2.0 (Async)
* **Migrations:** Alembic
* **Authentication:** OAuth2 with Password (JWT tokens)

### Frontend
* **Framework:** React (Vite)
* **Language:** TypeScript (Great for learning and robustness)
* **State/Data Management:** TanStack Query (React Query) for server state, Context API for local state.
* **Routing:** TanStack Router (Type-safe routing and first-class integration with TanStack Query).
* **Styling:** TailwindCSS (Premium aesthetic, dark mode support).
* **Icons:** Lucide React.

### Infrastructure
* **Database:** PostgreSQL 15 (Local installation or basic container just for DB).
* **Containerization:** Deferred for MVP 1. Focus on running locally via `uv` and `npm`.

---

## 3. Database Schema Design

### Users & Family
* **Family:** `id`, `name`, `invite_code`
* **User:** `id`, `family_id`, `username`, `password_hash`, `role` (ADMIN, MEMBER), `avatar_url`, `current_tokens`

### Calendar
* **Event:** `id`, `family_id`, `created_by`, `title`, `description`, `start_time`, `end_time`, `is_all_day`, `color_code`
* **EventAttendee:** `event_id`, `user_id`

### Chores & Tokens
* **Chore:** `id`, `family_id`, `title`, `description`, `definition_of_done`, `token_value`, `frequency` (daily, weekly, one-off), `image_url`
* **ChoreAssignment:** `id`, `chore_id`, `assigned_to` (user_id), `status` (PENDING, COMPLETED, APPROVED), `due_date`, `completed_at`
* **TokenTransaction:** `id`, `user_id`, `amount` (+/-), `description`, `created_at`

### Store
* **StoreItem:** `id`, `family_id`, `title`, `description`, `image_url`, `cost`, `stock` (optional)
* **Purchase:** `id`, `user_id`, `item_id`, `cost`, `status` (PENDING, APPROVED, FULFILLED), `created_at`

### Recipes & Meals
* **Recipe:** `id`, `family_id`, `title`, `description`, `image_url`, `servings`, `prep_time`, `cook_time`, `source_url`
* **Ingredient:** `id`, `recipe_id`, `name`, `quantity`, `unit`
* **Instruction:** `id`, `recipe_id`, `step_number`, `text`
* **MealPlan:** `id`, `family_id`, `date`, `recipe_id`, `meal_type` (Breakfast, Lunch, Dinner)

---

## 4. Implementation Phases

### Phase 1: Foundation & "uv" Setup
* **Repo Setup:** Git initialization.
* **Backend Init:**
    * Create `uv` project.
    * Setup FastAPI + Pydantic models.
* **Frontend Init:**
    * Vite + React + TailwindCSS.
    * Setup TanStack Query provider.
* **Database:** Setup Postgres container and SQLAlchemy connection.

### Phase 2: Authentication & Family Core
* **Models:** User and Family tables.
* **API:** Register, Login (JWT), Create/Join Family.
* **UI:** Landing page, Login form, Dashboard skeleton.

### Phase 3: The Calendar (Visual Core)
* **API:** CRUD for Events.
* **UI:** Build Month/Week/Day views using CSS Grid or a headless library.
* **Tech:** Integrate TanStack Query for fetching events based on view range.

### Phase 4: Chores & Token Economy
* **API:** Chore definitions, assignment logic, completion workflow.
* **UI (Parent):** Create chores, verify completion (approve for tokens).
* **UI (Child):** "My Chores" list, "Mark Done" action with earning animations.

### Phase 5: The Store
* **API:** Store inventory, Purchase transaction (atomic deduction of tokens).
* **UI:** Grid of rewards with "Buy" button and confirmation modal.
* **Notification:** Simple in-app alert for parents when a purchase is made.

### Phase 6: Recipes & Meal Prep
* **API:** Recipe schema + Scraper utility (beautifulsoup4).
* **UI:** Recipe card gallery, "Wake Lock" for cooking mode.
* **Meal Planner:** Drag-and-drop recipes onto the Calendar.
* **Shopping List:** Aggregation endpoint for ingredients based on meal range.

---

## 5. Development Workflow

### Backend (Python)

```bash
# Using uv
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install fastapi uvicorn sqlalchemy asyncpg alembic
uvicorn app.main:app --reload
```
